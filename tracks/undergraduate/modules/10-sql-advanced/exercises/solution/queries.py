"""분석형 SQL — 정답."""

Q1 = """
SELECT category, COUNT(*) AS cnt
FROM orders
GROUP BY category
HAVING COUNT(*) >= 3
ORDER BY category
"""

Q2 = """
SELECT id, amount
FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders)
ORDER BY id
"""

Q3 = """
SELECT id,
  CASE
    WHEN amount >= 20000 THEN 'high'
    WHEN amount >= 10000 THEN 'mid'
    ELSE 'low'
  END AS grade
FROM orders
ORDER BY id
"""

Q4 = """
SELECT c.name, SUM(o.amount) AS total
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name
HAVING SUM(o.amount) >= 20000
ORDER BY total DESC
"""

Q5 = """
SELECT id
FROM orders
WHERE customer_id IN (SELECT id FROM customers WHERE city = 'Seoul')
ORDER BY id
"""
