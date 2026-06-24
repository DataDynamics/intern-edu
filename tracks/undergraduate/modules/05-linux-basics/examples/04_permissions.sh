#!/bin/bash
# 예제 04 — 파일 권한 (chmod)
# 실행: bash 04_permissions.sh

cd /tmp
echo 'echo "I am executable"' > demo_script.sh

echo "== chmod 전 권한 =="
ls -l demo_script.sh

echo "== 직접 실행 시도 (실행권한 없음) =="
./demo_script.sh 2>/dev/null || echo "  실행 실패 — 실행권한(x)이 없기 때문"

echo "== chmod +x 로 실행권한 부여 =="
chmod +x demo_script.sh
ls -l demo_script.sh

echo "== 다시 실행 =="
./demo_script.sh

rm -f demo_script.sh
