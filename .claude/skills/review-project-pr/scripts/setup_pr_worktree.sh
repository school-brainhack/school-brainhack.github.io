#!/usr/bin/env bash
# Fetch a PR head and check it out into an isolated worktree for review.
# Usage: setup_pr_worktree.sh <PR-number>
# Prints the worktree path and the diff (name-status) vs origin/main.
set -euo pipefail

# Worktrees live under ~/git/brainhack-pr-review, alongside the pinned hugo
# binary that run_checks.sh downloads (bin/hugo, extended 0.128.0 = CI version).
PR="${1:?usage: setup_pr_worktree.sh <PR-number>}"
MAIN_REPO="/home/pbellec/git/school-brainhack.github.io"
WORKTREE="${HOME}/git/brainhack-pr-review/pr-${PR}"

cd "$MAIN_REPO"

git fetch origin "pull/${PR}/head:refs/pr-review/${PR}" --force
git fetch origin main

if [ -d "$WORKTREE" ]; then
  git worktree remove --force "$WORKTREE" 2>/dev/null || rm -rf "$WORKTREE"
fi
git worktree prune
mkdir -p "${HOME}/git/brainhack-pr-review"
git worktree add --force "$WORKTREE" "refs/pr-review/${PR}"

echo "WORKTREE=${WORKTREE}"
echo "--- files changed vs origin/main ---"
git -C "$WORKTREE" diff --name-status "origin/main...HEAD"
