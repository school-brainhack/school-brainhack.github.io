---
name: review-project-pr
description: This skill should be used when the user asks to review a Brainhack School pull request by number (e.g., "/review-project-pr 437" or "review PR 437"). It checks that the PR builds with Hugo, that images are not too heavy, that no stray files (notebooks, data) were added, that the frontmatter date is credible, that links work, and that the content has no typos or leftover garbage. It produces a review report in chat plus a local hugo serve link to inspect the rendered project page. Local-only — it never posts to GitHub.
---

# Review a Brainhack School project PR

Review a student-project PR against the site's conventions and produce a report the user can copy into PR feedback. Everything stays local: never comment on the PR, never push, never modify the main working tree.

## Environment facts

- Main repo: `/home/pbellec/git/school-brainhack.github.io` (remote `origin` = the upstream `school-brainhack` repo).
- Use the pinned Hugo at `~/git/brainhack-pr-review/bin/hugo` (extended 0.128.0, same version as CI; `run_checks.sh` auto-downloads it). Do NOT use `/usr/bin/hugo` (0.92, too old) or `/snap/bin/hugo` (0.164, rejects a duplicate YAML key in `config.yaml` that CI tolerates).
- Worktrees do not contain the theme submodule; always pass `--themesDir /home/pbellec/git/school-brainhack.github.io/themes` to hugo.

## Workflow

### 1. Fetch the PR into an isolated worktree

```bash
bash .claude/skills/review-project-pr/scripts/setup_pr_worktree.sh <PR#>
```

This creates `~/git/brainhack-pr-review/pr-<n>` and prints the files changed vs `origin/main`. Also grab metadata:

```bash
gh pr view <PR#> --json title,author,createdAt,body,url
```

### 2. Run the mechanical checks

```bash
bash .claude/skills/review-project-pr/scripts/run_checks.sh ~/git/brainhack-pr-review/pr-<n>
```

This prints `[BUILD]`, `[IMAGES]`, `[STRAY]`, and `[LINKS]` sections with PASS/WARN/FAIL lines. Interpret them; downgrade link FAILs to WARN when the site is known to block bots.

### 3. Qualitative review

Read `references/checklist.md` for the full rubric, then read the PR's `index.md` in the worktree and check:

- **Date credibility**: frontmatter `date:` vs the PR's `createdAt` and the current school edition.
- **Frontmatter conventions**: `type: "project"`, lowercase tags, ~75-word summary, `image:` file exists, hyphenated slug.
- **Internal links/images**: relative references in `index.md` resolve, and the built page under `<worktree>/public/project/<slug>/` contains them.
- **Typos**: genuine misspellings/grammar errors with locations — not style nits.
- **Garbage**: leftover template text, duplicated blocks, broken shortcodes, merge-conflict markers, secrets, unrelated content.

### 4. Serve the preview

Kill any previous preview, then start hugo serve in the background on port 1414 (1313 is left free for the user's own serve):

```bash
pkill -f "hugo serve.*1414" 2>/dev/null
cd ~/git/brainhack-pr-review/pr-<n> && ~/git/brainhack-pr-review/bin/hugo serve --port 1414 --bind 127.0.0.1 \
  --themesDir /home/pbellec/git/school-brainhack.github.io/themes
```

Run it with `run_in_background: true`. Determine the slug's rendered URL path (Hugo lowercases it) and include `http://localhost:1414/project/<slug>/` in the report.

### 5. Report

Use the report template at the end of `references/checklist.md`: lead with an overall verdict (✅ / ⚠️ / ❌), then a summary table, then findings written so they can be copy-pasted as PR feedback, then the preview link.

## Cleanup

Reviewing the same PR again refreshes the same worktree automatically. To clean up manually: `git worktree remove --force ~/git/brainhack-pr-review/pr-<n>` from the main repo.
