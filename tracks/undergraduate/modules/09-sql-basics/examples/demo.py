"""예제 — SQLite로 SELECT/WHERE/ORDER BY/JOIN/GROUP BY 시연
실행: python demo.py   (schema.sql을 메모리 DB에 적재)
"""
import sqlite3

conn = sqlite3.connect(":memory:")
with open("schema.sql", "r", encoding="utf-8") as f:
    conn.executescript(f.read())


def run(title, sql):
    print(f"\n== {title} ==")
    for row in conn.execute(sql):
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
