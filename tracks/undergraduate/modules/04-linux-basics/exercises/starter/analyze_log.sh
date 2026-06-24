#!/bin/bash
# 실습 — 접속 로그 분석 스크립트
# 실행: chmod +x analyze_log.sh && ./analyze_log.sh

LOG="data/access.log"

# 로그 파일이 있는지 먼저 확인 (조건문)
if [ ! -f "$LOG" ]; then
  echo "오류: $LOG 를 찾을 수 없습니다. starter 폴더에서 실행하세요."
  exit 1
fi

echo "===== 접속 로그 분석 결과 ====="

echo
echo "[1] 총 요청 수"
# TODO: $LOG의 전체 줄 수를 출력하세요 (힌트: wc -l)


echo
echo "[2] 상태코드별 빈도"
# TODO: 9번째 필드(상태코드)를 뽑아 빈도순으로 출력하세요
#       힌트: awk '{print $9}' "$LOG" | sort | uniq -c | sort -rn


echo
echo "[3] 에러 요청 수 (상태코드 400 이상)"
# TODO: 상태코드가 400 이상인 줄의 개수를 출력하세요
#       힌트: awk '$9 >= 400' "$LOG" | wc -l


echo
echo "[4] 가장 많이 접속한 IP Top 5"
# TODO: 1번째 필드(IP)를 뽑아 빈도순 상위 5개를 출력하세요
#       힌트: awk '{print $1}' ... | sort | uniq -c | sort -rn | head -5

