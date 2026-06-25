#!/usr/bin/env bash
# Northwind(고전적인 e-커머스/ERP 샘플)를 로컬 PostgreSQL에 적재합니다.
#
# 사전 준비:
#   - PostgreSQL 실행 (설치: ../../setup/postgresql-setup.md)
#   - psql / curl 사용 가능
#
# 접속 정보는 PG* 환경변수(PGHOST/PGPORT/PGUSER/PGPASSWORD)로 바꿀 수 있습니다.
# 데이터베이스 이름은 NORTHWIND_DB 로 바꿀 수 있습니다(기본: northwind).
# 덤프에는 CREATE DATABASE 가 없으므로 스크립트가 먼저 DB를 만듭니다.
set -euo pipefail
cd "$(dirname "$0")"

DB="${NORTHWIND_DB:-northwind}"
URL="https://raw.githubusercontent.com/pthom/northwind_psql/master/northwind.sql"

echo "▶ 데이터베이스 '$DB' 준비 (없으면 생성)"
psql -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB'" | grep -q 1 || createdb "$DB"

echo "▶ Northwind 스키마/데이터 적재 중..."
curl -fsSL "$URL" | psql -d "$DB" -v ON_ERROR_STOP=1 -q

echo "✅ 완료. 접속:  psql -d $DB"
echo "   예) 상품별 매출 Top 10:"
echo "       SELECT p.product_name, SUM(od.unit_price*od.quantity*(1-od.discount)) AS revenue"
echo "       FROM order_details od JOIN products p ON p.product_id = od.product_id"
echo "       GROUP BY p.product_name ORDER BY revenue DESC LIMIT 10;"
