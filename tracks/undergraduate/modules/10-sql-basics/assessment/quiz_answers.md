# 모듈 10 — 퀴즈 정답

1. 기본키는 한 테이블에서 각 행을 **유일하게 식별**하는 열, 외래키는 **다른 테이블의 기본키를 참조**해 관계를 맺는 열.
2. `WHERE`는 그룹화 **전** 개별 행을 필터, `HAVING`은 `GROUP BY` **후** 그룹을 필터.
3. `INNER JOIN`은 양쪽 모두 매칭되는 행만, `LEFT JOIN`은 왼쪽 테이블 전부 + 매칭 없으면 오른쪽은 NULL.
4. `FROM → WHERE → GROUP BY → SELECT` (그 뒤 ORDER BY → LIMIT).
5. customers의 **중복 제거된 도시 목록**.

6. `SELECT name FROM customers WHERE city = 'Busan';`
7. `SELECT * FROM orders WHERE category = 'book' ORDER BY amount DESC;`
8. `SELECT amount FROM orders ORDER BY amount DESC LIMIT 1;`
9.
   ```sql
   SELECT c.name, COUNT(*) AS cnt
   FROM customers c
   JOIN orders o ON o.customer_id = c.id
   GROUP BY c.id, c.name;
   ```
10.
   ```sql
   SELECT city, COUNT(*) AS cnt
   FROM customers
   GROUP BY city
   ORDER BY cnt DESC;
   ```
