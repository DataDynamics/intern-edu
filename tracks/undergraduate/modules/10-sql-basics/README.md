# 모듈 10 — SQL 기초

> **포커스**: 관계형 DB 개념, SELECT / WHERE / ORDER BY, JOIN
> **예상 기간**: 1주
> **선행 모듈**: 09 파일 & 데이터 포맷

데이터는 대부분 **데이터베이스**에 저장됩니다. SQL은 그 데이터를 묻고 꺼내는
공용어입니다. 데이터 엔지니어에게 SQL은 Python만큼 중요합니다. 이 모듈은 설치 없이
바로 쓸 수 있는 **SQLite**로 SELECT부터 JOIN까지 손에 익힙니다.

> 💡 SQLite는 Python에 기본 내장(`import sqlite3`)되어 있어 별도 설치가 필요 없습니다.
> 실무에서는 PostgreSQL 등을 쓰지만 SQL 문법은 대부분 동일합니다. (모듈 12에서 Postgres 사용)

---

## 🎯 학습 목표
- 테이블·행·열·기본키/외래키 등 관계형 DB의 기본 개념을 이해한다
- `SELECT ... FROM ... WHERE`로 원하는 데이터를 조회한다
- `ORDER BY`, `LIMIT`으로 정렬·제한한다
- `JOIN`으로 두 테이블을 연결해 조회한다
- `GROUP BY`로 그룹별 집계를 한다 (개수/합계)

---

## 📚 핵심 주제

### 1. 관계형 데이터베이스 개념
- **테이블(table)**: 행(row)과 열(column)로 된 표. 하나의 개체(예: 고객, 주문)를 표현
- **기본키(Primary Key)**: 각 행을 유일하게 식별 (예: `customers.id`)
- **외래키(Foreign Key)**: 다른 테이블을 가리키는 열 (예: `orders.customer_id → customers.id`)
- 테이블을 **관계(외래키)** 로 연결하는 것이 "관계형"의 핵심

예시 스키마:
```
customers(id, name, city)
orders(id, customer_id, category, amount)   -- customer_id가 customers.id를 참조
```

### 2. SELECT 기본
```sql
SELECT * FROM customers;                 -- 모든 열
SELECT name, city FROM customers;        -- 특정 열만
SELECT DISTINCT city FROM customers;     -- 중복 제거
```

### 3. WHERE — 조건 필터
```sql
SELECT * FROM orders WHERE amount >= 10000;
SELECT * FROM orders WHERE category = 'book';
SELECT * FROM orders WHERE amount BETWEEN 5000 AND 15000;
SELECT * FROM customers WHERE city IN ('Seoul', 'Busan');
SELECT * FROM customers WHERE name LIKE '김%';   -- '김'으로 시작
```
비교/논리: `= != < > <= >=`, `AND`, `OR`, `NOT`.

### 4. ORDER BY / LIMIT
```sql
SELECT * FROM orders ORDER BY amount DESC;        -- 금액 내림차순
SELECT * FROM orders ORDER BY category, amount;   -- 다중 정렬
SELECT * FROM orders ORDER BY amount DESC LIMIT 3;-- 상위 3건
```

### 5. JOIN — 테이블 연결 ⭐
서로 다른 테이블의 데이터를 외래키로 이어 한 번에 조회합니다.
```sql
-- 각 주문에 고객 이름을 붙여서 조회
SELECT o.id, c.name, o.category, o.amount
FROM orders o
JOIN customers c ON o.customer_id = c.id;
```
- `INNER JOIN`(기본): 양쪽 모두 매칭되는 행만
- `LEFT JOIN`: 왼쪽 테이블은 모두 + 매칭 없으면 오른쪽은 NULL
- `o`, `c`는 **별칭(alias)** — 테이블 이름을 짧게

### 6. GROUP BY — 그룹별 집계
```sql
-- 카테고리별 매출 합계와 주문 수
SELECT category, SUM(amount) AS total, COUNT(*) AS cnt
FROM orders
GROUP BY category
ORDER BY total DESC;
```
집계 함수: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
> 📌 그룹 자체를 조건으로 거를 땐 `WHERE`가 아니라 `HAVING`을 씁니다. (모듈 11에서 심화)

### 7. SQL 작성 순서 vs 실행 순서
```
작성: SELECT → FROM → WHERE → GROUP BY → ORDER BY → LIMIT
실행: FROM → WHERE → GROUP BY → SELECT → ORDER BY → LIMIT
```
실행 순서를 알면 "왜 SELECT의 별칭을 WHERE에서 못 쓰는지" 같은 헷갈림이 풀립니다.

---

## 🛠 실습 / 산출물
`exercises/`에서 SQLite DB(고객·주문)를 대상으로 **질문에 답하는 SQL 쿼리**를 작성합니다.
- 특정 조건의 주문 조회, 금액순 정렬, 고객-주문 JOIN, 카테고리별 집계 등
- `queries.py`의 각 쿼리를 채우면 `check.py`가 실제 DB에 실행해 정답과 비교
- 산출물: `check.py`를 통과하는 `queries.py`

---

## ✅ 완료 기준 (체크리스트)
- [ ] 테이블/기본키/외래키 개념을 설명할 수 있다
- [ ] WHERE로 조건에 맞는 행을 조회할 수 있다
- [ ] ORDER BY/LIMIT으로 정렬·상위 N건을 뽑을 수 있다
- [ ] 두 테이블을 JOIN으로 연결해 조회할 수 있다
- [ ] GROUP BY로 그룹별 합계/개수를 구할 수 있다
- [ ] `exercises/`의 `queries.py`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — SQLite를 세팅하고 쿼리를 실행하는 예제 (`schema.sql`, `demo.py`)
- `exercises/starter/` — 채워야 할 쿼리 골격 + 자가 검증
- `exercises/solution/` — 정답 쿼리
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [SQLBolt — 인터랙티브 SQL 연습](https://sqlbolt.com/)
- [SQLite 공식 문서](https://www.sqlite.org/lang.html)
- [Mode SQL 튜토리얼](https://mode.com/sql-tutorial/)
- 모듈 11(SQL 활용 — 집계/서브쿼리)로 이어집니다.
