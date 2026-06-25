#!/usr/bin/env bash
# Pagila(Sakila의 PostgreSQL 네이티브 포트 — DVD 대여점)를 로컬 PostgreSQL에 적재합니다.
#
# 사전 준비:
#   - PostgreSQL 실행 (설치: ../../setup/postgresql-setup.md)
#   - psql / curl 사용 가능
#
# 접속 정보는 PG* 환경변수(PGHOST/PGPORT/PGUSER/PGPASSWORD)로 바꿀 수 있습니다.
# 데이터베이스 이름은 PAGILA_DB 로 바꿀 수 있습니다(기본: pagila).
# 스키마 → 데이터 순서로 두 파일을 적재합니다.
set -euo pipefail
cd "$(dirname "$0")"

DB="${PAGILA_DB:-pagila}"
BASE="https://raw.githubusercontent.com/devrimgunduz/pagila/master"

echo "▶ 데이터베이스 '$DB' 준비 (없으면 생성)"
psql -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB'" | grep -q 1 || createdb "$DB"

echo "▶ 스키마 적재..."
curl -fsSL "$BASE/pagila-schema.sql" | psql -d "$DB" -v ON_ERROR_STOP=1 -q
echo "▶ 데이터 적재... (약 3MB)"
curl -fsSL "$BASE/pagila-data.sql"   | psql -d "$DB" -v ON_ERROR_STOP=1 -q

echo "✅ 완료. 접속:  psql -d $DB"
echo "   예) 카테고리별 대여 건수:"
echo "       SELECT c.name, COUNT(*) AS rentals"
echo "       FROM rental r JOIN inventory i ON i.inventory_id = r.inventory_id"
echo "       JOIN film_category fc ON fc.film_id = i.film_id"
echo "       JOIN category c ON c.category_id = fc.category_id"
echo "       GROUP BY c.name ORDER BY rentals DESC;"
