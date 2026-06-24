#!/bin/bash
# 예제 02 — 브랜치 생성 → 작업 → main에 병합 (PR의 로컬 버전)
# 실행: bash 02_branch_and_merge.sh
set -e
DEMO=/tmp/git-branch-demo
rm -rf "$DEMO"; mkdir -p "$DEMO"; cd "$DEMO"
git init -q -b main
git config user.email "demo@example.com"; git config user.name "Demo"
echo "# Project" > README.md
git add . && git commit -q -m "Initial commit"

echo "== feature 브랜치 생성 & 이동 =="
git switch -c feature/add-greeting
echo "greeting = 'hi'" > greeting.py
git add . && git commit -q -m "Add greeting"
git log --oneline --all

echo "== main으로 병합 (PR 승인 후 merge에 해당) =="
git switch main
git merge --no-ff -q feature/add-greeting -m "Merge feature/add-greeting"
git log --oneline --graph

rm -rf "$DEMO"
