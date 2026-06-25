"""예제 — PostgreSQL로 SELECT/WHERE/ORDER BY/JOIN/GROUP BY 시연

사전 준비:
  1. PostgreSQL 실행 (설치는 setup/postgresql-setup.md 참고)
  2. pip install psycopg2-binary

실행: python demo.py   (schema.sql을 현재 접속 DB에 적재 후 쿼리 시연)

접속 정보는 환경변수로 바꿀 수 있습니다.
  - DATABASE_URL=postgresql://사용자:비밀번호@localhost:5432/DB이름
  - 또는 PGHOST/PGPORT/PGUSER/PGPASSWORD/PGDATABASE
  - 아무것도 없으면 libpq 기본값(현재 OS 사용자)으로 접속합니다.
"""
import os
import psycopg2

conn = psycopg2.connect(os.environ.get("DATABASE_URL", ""))
conn.autocommit = True
with conn.cursor() as cur, open("schema.sql", "r", encoding="utf-8") as f:
    cur.execute(f.read())


def run(title, sql):
    print(f"\n== {title} ==")
    with conn.cursor() as cur:
        cur.execute(sql)
        for row in cur.fetchall():
            print("  ", row)


run("전체 고객", "SELECT * FROM customers")
run("WHERE: 1만원 이상 주문", "SELECT id, category, amount FROM orders WHERE amount >= 10000")
run("ORDER BY + LIMIT: 비싼 주문 Top 3",
    "SELECT id, category, amount FROM orders ORDER BY amount DESC LIMIT 3")
run("JOIN: 주문 + 고객이름",
    """SELECT o.id, c.name, o.category, o.amount
       FROM orders o JOIN customers c ON o.customer_id = c.id
       ORDER BY o.id""")
run("GROUP BY: 카테고리별 매출",
    """SELECT category, SUM(amount) AS total, COUNT(*) AS cnt
       FROM orders GROUP BY category ORDER BY total DESC""")

conn.close()
