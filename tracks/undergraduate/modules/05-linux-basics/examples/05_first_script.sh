#!/bin/bash
# 예제 05 — 변수, 조건문, 반복문을 쓴 첫 스크립트
# 실행: bash 05_first_script.sh

LOG="data/access.log"

# 변수
THRESHOLD=400

echo "== 파일 존재 확인 (조건문) =="
if [ -f "$LOG" ]; then
  echo "로그 파일 발견: $LOG ($(wc -l < "$LOG") 줄)"
else
  echo "로그 파일이 없습니다. examples/ 폴더에서 실행하세요."
  exit 1
fi

echo "== 상태코드 ${THRESHOLD} 이상(에러)인 요청 나열 (반복문) =="
count=0
while read -r line; do
  status=$(echo "$line" | awk '{print $9}')
  if [ "$status" -ge "$THRESHOLD" ]; then
    echo "  [에러 $status] $(echo "$line" | awk '{print $1, $7}')"
    count=$((count + 1))
  fi
done < "$LOG"
echo "총 에러 요청: ${count}건"
