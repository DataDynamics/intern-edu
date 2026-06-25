#!/usr/bin/env bash
# Chinook(디지털 음악 스토어) 데이터셋을 로컬 PostgreSQL에 적재합니다.
#
# 사전 준비:
#   - PostgreSQL 실행 (설치: ../../setup/postgresql-setup.md)
#   - psql / curl 사용 가능
#
# 접속 정보는 PG* 환경변수(PGHOST/PGPORT/PGUSER/PGPASSWORD)로 바꿀 수 있습니다.
# 이 SQL 덤프는 스스로 `DROP DATABASE IF EXISTS chinook; CREATE DATABASE chinook;`
# 를 수행하므로, 유지보수용 DB(postgres)에 접속해 실행합니다.
set -euo pipefail
cd "$(dirname "$0")"

URL="https://raw.githubusercontent.com/lerocha/chinook-database/master/ChinookDatabase/DataSources/Chinook_PostgreSql.sql"

echo "▶ Chinook 덤프 내려받아 적재 중 (DB 'chinook' 자동 생성/재생성)..."
curl -fsSL "$URL" | psql -d postgres -v ON_ERROR_STOP=1 -q

echo "✅ 완료. 접속:  psql -d chinook"
echo "   예) 가장 많이 팔린 트랙 Top 10:"
echo "       SELECT t.name, SUM(il.quantity) AS sold"
echo "       FROM invoice_line il JOIN track t ON t.track_id = il.track_id"
echo "       GROUP BY t.name ORDER BY sold DESC LIMIT 10;"
