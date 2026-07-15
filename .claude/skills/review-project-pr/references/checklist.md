# Review rubric for Brainhack School project PRs

## Expected PR shape

A student project PR should add exactly one directory `content/en/project/<slug>/` containing:
- `index.md` (required)
- one or a few reasonably-sized images (cover + optional figures)

Anything else (changes to config, layouts, other projects, data files) is a red flag unless the PR description explains it.

## Frontmatter expectations (`index.md`)

```yaml
type: "project"                      # required, exactly this value
date: "YYYY-MM-DD"                   # see date credibility below
title: "Project Title"
names: [Author1, Author2]            # real author names
github_repo: "https://github.com/..."  # should exist (checked by link check)
website: ""                          # optional
tags: [tag1, tag2]                   # LOWERCASE only — flag any uppercase tag
summary: "~75 word description"      # flag if <30 or >120 words (breaks listing cards)
image: "cover.png"                   # optional; if present, the file MUST exist in the same directory
```

Directory slug: hyphens, no spaces. Lowercase preferred; mixed case works but note it.

## Date credibility

Compare frontmatter `date:` against the PR's `createdAt` (from `gh pr view`):
- FAIL if the date is after the PR was opened by more than a few days, or in a different year than the current school edition.
- WARN if it differs from the PR open date by more than ~2 months.
- The date should plausibly correspond to when the project was done (during the school, near PR opening).

## Image weight

- PASS ≤ 500 KB per image
- WARN > 500 KB (suggest compression: `optipng`, `jpegoptim`, resizing)
- FAIL > 1.5 MB (must be fixed before merge)

## Stray files (FAIL)

`.ipynb`, `.ipynb_checkpoints/`, `.DS_Store`, `Thumbs.db`, `__pycache__/`, `*.pyc`, editor swap files, `node_modules/`, archives (`.zip`, `.tar.gz`), and data files (`.csv`, `.tsv`, `.nii`, `.nii.gz`, `.mat`, `.pkl`, `.npy`, `.h5`). Notebooks and data belong in the student's own project repo, not the website.

## Links

- External links: checked mechanically by `run_checks.sh` (curl). 403/405/429/999 responses are often bot-blocking, not breakage — verify by eye or note as WARN.
- Internal links and image references: verify manually that each relative path referenced in `index.md` (markdown `![](...)` and HTML `<img src=...>`) exists in the project directory, and that the rendered page in `public/project/<slug>/` includes the images.

## Typos and garbage

- Typos: read the prose; report genuine misspellings and grammar errors with the exact line. Do not nitpick style or non-native phrasing that is still clear.
- Garbage: leftover template placeholder text (e.g., text copied from the project template or another project without edits), lorem ipsum, duplicated sections, broken shortcodes/HTML, merge-conflict markers (`<<<<<<<`), secrets or tokens, content unrelated to the project.

## Report template

```markdown
## Review of PR #<n> — <title>

**Verdict: ✅ ready to merge / ⚠️ minor fixes needed / ❌ needs work**

| Check | Result |
|---|---|
| Build | ✅/⚠️/❌ |
| Image weight | ... |
| Stray files | ... |
| Date credibility | ... |
| Links | ... |
| Typos | ... |
| Content quality | ... |

### Findings
(one short subsection per non-PASS check, with exact files/lines and the suggested fix,
written so it can be copy-pasted as PR feedback)

### Preview
Rendered project page: http://localhost:1414/project/<slug>/
```

Verdict rule of thumb: any FAIL → ❌; only WARNs/typos → ⚠️; all clean → ✅.
