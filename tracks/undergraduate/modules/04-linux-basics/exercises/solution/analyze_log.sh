#!/bin/bash
# 정답 — 접속 로그 분석 스크립트
# 실행: chmod +x analyze_log.sh && ./analyze_log.sh

LOG="data/access.log"

if [ ! -f "$LOG" ]; then
  echo "오류: $LOG 를 찾을 수 없습니다. solution 폴더에서 실행하세요."
  exit 1
fi

echo "===== 접속 로그 분석 결과 ====="

echo
echo "[1] 총 요청 수"
wc -l < "$LOG"

echo
echo "[2] 상태코드별 빈도"
awk '{print $9}' "$LOG" | sort | uniq -c | sort -rn

echo
echo "[3] 에러 요청 수 (상태코드 400 이상)"
awk '$9 >= 400' "$LOG" | wc -l

echo
echo "[4] 가장 많이 접속한 IP Top 5"
awk '{print $1}' "$LOG" | sort | uniq -c | sort -rn | head -5
