"""정답 SQL 쿼리."""

Q1 = "SELECT name, city FROM customers"

Q2 = "SELECT id, amount FROM orders WHERE amount >= 10000"

Q3 = "SELECT id, amount FROM orders ORDER BY amount DESC LIMIT 3"

Q4 = "SELECT name FROM customers WHERE city = 'Seoul'"

Q5 = """
SELECT o.id, c.name, o.amount
FROM orders o
JOIN customers c ON o.customer_id = c.id
ORDER BY o.id
"""

Q6 = """
SELECT category, SUM(amount) AS total
FROM orders
GROUP BY category
ORDER BY total DESC
"""
