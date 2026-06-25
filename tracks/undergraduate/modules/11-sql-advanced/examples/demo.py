"""예제 — 집계 심화 / HAVING / 서브쿼리 / CASE / 인덱스 (PostgreSQL)

사전 준비:
  1. PostgreSQL 실행 (설치는 setup/postgresql-setup.md 참고)
  2. pip install psycopg2-binary

실행: python demo.py

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


run("전체 집계", "SELECT COUNT(*) cnt, SUM(amount) total, AVG(amount) avg FROM orders")
run("HAVING: 평균 1만원 이상 카테고리",
    """SELECT category, AVG(amount) avg_amount FROM orders
       GROUP BY category HAVING AVG(amount) >= 10000 ORDER BY avg_amount DESC""")
run("서브쿼리: 전체 평균보다 비싼 주문",
    "SELECT id, amount FROM orders WHERE amount > (SELECT AVG(amount) FROM orders) ORDER BY id")
run("IN 서브쿼리: Seoul 고객의 주문 수",
    """SELECT COUNT(*) FROM orders
       WHERE customer_id IN (SELECT id FROM customers WHERE city='Seoul')""")
run("CASE: 금액 등급",
    """SELECT id, amount,
         CASE WHEN amount>=20000 THEN 'high'
              WHEN amount>=10000 THEN 'mid' ELSE 'low' END AS grade
       FROM orders ORDER BY id LIMIT 5""")

print("\n== 인덱스 생성 후 실행계획 ==")
with conn.cursor() as cur:
    cur.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id)")
    cur.execute("EXPLAIN SELECT * FROM orders WHERE customer_id = 1")
    for row in cur.fetchall():
        print("  ", row)

conn.close()
