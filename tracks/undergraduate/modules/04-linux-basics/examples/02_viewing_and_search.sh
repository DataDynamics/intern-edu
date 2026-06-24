#!/bin/bash
# 예제 02 — 파일 내용 보기 & 검색 (cat/head/tail/grep)
# 실행: bash 02_viewing_and_search.sh

LOG="data/access.log"

echo "== 앞 3줄 =="
head -n 3 "$LOG"

echo "== 뒤 3줄 =="
tail -n 3 "$LOG"

echo "== 전체 줄 수 =="
wc -l "$LOG"

echo "== 403(권한거부) 요청만 보기 =="
grep " 403 " "$LOG"

echo "== ERROR성(500) 요청 개수 =="
grep -c " 500 " "$LOG"
