#!/bin/bash
# 예제 03 — 파이프와 리다이렉션 (핵심!)
# 실행: bash 03_pipes_and_redirection.sh

LOG="data/access.log"

echo "== 상태코드별 빈도 (Top) =="
# $9 = Common Log Format에서 9번째 필드 = 상태코드
awk '{print $9}' "$LOG" | sort | uniq -c | sort -rn

echo "== 가장 많이 접속한 IP Top 3 =="
awk '{print $1}' "$LOG" | sort | uniq -c | sort -rn | head -3

echo "== 결과를 파일로 저장 (리다이렉션 >) =="
awk '{print $1}' "$LOG" | sort | uniq -c | sort -rn > /tmp/top_ips.txt
echo "저장된 파일 내용:"
cat /tmp/top_ips.txt
rm -f /tmp/top_ips.txt
