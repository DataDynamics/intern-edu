"""예제 — 집계 심화 / HAVING / 서브쿼리 / CASE / 인덱스
실행: python demo.py
"""
import sqlite3

conn = sqlite3.connect(":memory:")
with open("schema.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())


def run(title, sql):
    print(f"\n== {title} ==")
    for row in conn.execute(sql):
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
conn.execute("CREATE INDEX idx_orders_customer ON orders(customer_id)")
for row in conn.execute("EXPLAIN QUERY PLAN SELECT * FROM orders WHERE customer_id = 1"):
    print("  ", row)

conn.close()
