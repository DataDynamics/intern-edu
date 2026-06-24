#!/bin/bash
# 예제 01 — git 기본 흐름을 임시 저장소에서 시연
# 실행: bash 01_basic_flow.sh  (실제 교육 repo를 건드리지 않고 /tmp에서 동작)
set -e
DEMO=/tmp/git-demo
rm -rf "$DEMO"; mkdir -p "$DEMO"; cd "$DEMO"

echo "== git init =="
git init -q
git config user.email "demo@example.com"
git config user.name "Demo"

echo "== 파일 생성 후 상태 확인 =="
echo "print('hello')" > app.py
git status --short          # ?? app.py  (추적 안 됨)

echo "== add → staging =="
git add app.py
git status --short          # A  app.py  (스테이징됨)

echo "== commit =="
git commit -q -m "Add hello app"
git log --oneline

echo "== 수정 후 diff =="
echo "print('world')" >> app.py
git diff

echo "== 두 번째 커밋 =="
git add app.py
git commit -q -m "Print world too"
git log --oneline

rm -rf "$DEMO"
