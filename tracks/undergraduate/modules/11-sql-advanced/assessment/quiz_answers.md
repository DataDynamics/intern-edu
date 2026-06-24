# 모듈 11 — 퀴즈 정답

1. `WHERE`는 그룹화 전 **개별 행**을 거름(예: `WHERE amount>1000`), `HAVING`은 `GROUP BY` 후 **그룹**을 거름(예: `HAVING SUM(amount)>10000`).
2. 단일 값을 반환하는 서브쿼리. 예: `WHERE amount > (SELECT AVG(amount) FROM orders)`.
3. 행마다 조건에 따라 다른 값을 부여(분류/라벨링)하거나, 조건부 집계를 할 때.
4. NULL은 "값 없음"이라 어떤 값과도 같다/다르다를 판단할 수 없음 → `IS NULL` / `IS NOT NULL` 사용.
5. 장점: WHERE/JOIN 조회 속도 향상 / 비용: 저장공간 증가, INSERT·UPDATE 시 인덱스 갱신 부담.

6.
   ```sql
   SELECT category, MAX(amount) AS max_amount
   FROM orders GROUP BY category
   HAVING MAX(amount) >= 20000;
   ```
7.
   ```sql
   SELECT * FROM orders
   WHERE amount > (SELECT AVG(amount) FROM orders WHERE category='toy');
   ```
8.
   ```sql
   SELECT id, amount,
     CASE WHEN amount >= 10000 THEN 'big' ELSE 'small' END AS label
   FROM orders;
   ```
9.
   ```sql
   SELECT c.id, c.name
   FROM customers c
   LEFT JOIN orders o ON o.customer_id = c.id
   WHERE o.id IS NULL;
   -- (이 데이터셋에서는 결과가 없음 — 모든 고객이 주문 있음)
   ```
10. `CREATE INDEX idx_orders_category ON orders(category);`
