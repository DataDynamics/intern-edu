#!/bin/bash
# 예제 01 — 이동, 탐색, 파일/디렉토리 조작
# 실행: bash 01_navigation_and_files.sh

echo "== 현재 위치 =="
pwd

echo "== 파일 목록 (상세) =="
ls -al

echo "== 임시 작업공간 만들기 =="
mkdir -p /tmp/linux-demo/data
cd /tmp/linux-demo
echo "now at: $(pwd)"

echo "== 파일 생성/복사/이동 =="
touch report.txt
echo "hello data engineering" > report.txt
cp report.txt data/report_backup.txt
mv report.txt data/report.txt
ls -R /tmp/linux-demo

echo "== 정리(삭제) =="
rm -r /tmp/linux-demo
echo "삭제 완료. 존재 여부:"
ls /tmp/linux-demo 2>/dev/null || echo "  (없음 — 정상)"
