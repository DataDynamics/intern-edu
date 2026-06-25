#!/usr/bin/env bash
# shop 샘플을 로컬 PostgreSQL에 적재합니다.
#
# 사전 준비:
#   - PostgreSQL 실행 (설치: ../../setup/postgresql-setup.md)
#   - psql 사용 가능
#
# 접속 정보는 PG* 환경변수(PGHOST/PGPORT/PGUSER/PGPASSWORD)로 바꿀 수 있습니다.
# 적재할 데이터베이스 이름은 SHOP_DB 로 바꿀 수 있습니다(기본: shop).
set -euo pipefail
cd "$(dirname "$0")"

DB="${SHOP_DB:-shop}"

echo "▶ 데이터베이스 '$DB' 준비 (없으면 생성)"
psql -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB'" | grep -q 1 || createdb "$DB"

echo "▶ 스키마 생성 + CSV 적재"
psql -d "$DB" -v ON_ERROR_STOP=1 -q -f load.sql

echo "✅ 완료. 접속:  psql -d $DB"
echo "   예) 카테고리별 매출:"
echo "       SELECT p.category, SUM(oi.quantity*oi.unit_price) AS revenue"
echo "       FROM order_items oi JOIN products p ON p.id = oi.product_id"
echo "       GROUP BY p.category ORDER BY revenue DESC;"
