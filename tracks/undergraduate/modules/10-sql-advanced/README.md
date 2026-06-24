# 모듈 10 — SQL 활용

> **포커스**: 집계 심화(GROUP BY/HAVING), 서브쿼리, CASE, 인덱스 개념
> **예상 기간**: 1주
> **선행 모듈**: 09 SQL 기초

기초 SELECT/JOIN을 넘어, 데이터에서 **의미 있는 답을 끌어내는** SQL을 배웁니다.
"카테고리별 평균이 1만원 넘는 것만", "전체 평균보다 비싼 주문", "조건에 따라 라벨 붙이기"
같은 분석형 쿼리가 데이터 엔지니어의 일상입니다. 마지막으로 **인덱스**로 쿼리가 왜
빨라지는지도 감을 잡습니다.

> 💡 09와 동일하게 SQLite로 실습합니다. 데이터는 조금 더 풍부해집니다.

---

## 🎯 학습 목표
- 집계 함수와 `GROUP BY`/`HAVING`으로 그룹을 분석한다
- 서브쿼리(쿼리 안의 쿼리)로 단계적 문제를 푼다
- `CASE WHEN`으로 조건부 분류/라벨링을 한다
- `NULL`을 올바르게 다룬다
- 인덱스가 조회 성능에 주는 영향을 개념적으로 이해한다

---

## 📚 핵심 주제

### 1. 집계 함수 복습 + 별칭
```sql
SELECT
  COUNT(*)      AS cnt,
  SUM(amount)   AS total,
  AVG(amount)   AS avg_amount,
  MIN(amount)   AS min_amount,
  MAX(amount)   AS max_amount
FROM orders;
```

### 2. GROUP BY + HAVING ⭐
`WHERE`는 **행**을 거르고, `HAVING`은 **그룹**을 거릅니다.
```sql
-- 카테고리별 평균 주문액이 10000 이상인 카테고리만
SELECT category, AVG(amount) AS avg_amount
FROM orders
GROUP BY category
HAVING AVG(amount) >= 10000
ORDER BY avg_amount DESC;
```
순서: `WHERE`(행 필터) → `GROUP BY` → `HAVING`(그룹 필터).

### 3. 서브쿼리 (Subquery)
쿼리 결과를 다른 쿼리의 입력으로 씁니다.
```sql
-- (a) 스칼라 서브쿼리: 전체 평균보다 비싼 주문
SELECT id, amount
FROM orders
WHERE amount > (SELECT AVG(amount) FROM orders);

-- (b) IN 서브쿼리: 'Seoul' 고객이 낸 주문만
SELECT * FROM orders
WHERE customer_id IN (SELECT id FROM customers WHERE city = 'Seoul');

-- (c) FROM 절 서브쿼리(파생 테이블): 고객별 합계 중 상위
SELECT name, total FROM (
    SELECT c.name, SUM(o.amount) AS total
    FROM customers c JOIN orders o ON o.customer_id = c.id
    GROUP BY c.id, c.name
) AS t
WHERE total >= 20000;
```

### 4. CASE WHEN — 조건부 분류
```sql
SELECT id, amount,
  CASE
    WHEN amount >= 20000 THEN 'high'
    WHEN amount >= 10000 THEN 'mid'
    ELSE 'low'
  END AS grade
FROM orders;
```
집계와 함께 쓰면 "조건부 개수 세기"도 가능합니다.
```sql
SELECT
  SUM(CASE WHEN amount >= 10000 THEN 1 ELSE 0 END) AS big_orders,
  COUNT(*) AS total
FROM orders;
```

### 5. NULL 다루기
- `NULL`은 "값 없음". `= NULL`이 아니라 `IS NULL` / `IS NOT NULL`로 비교
- `COUNT(column)`은 NULL을 세지 않음 (`COUNT(*)`는 전체 행)
- `COALESCE(value, 0)` : NULL이면 대체값 사용

### 6. 인덱스 (Index) 개념
- 인덱스는 책의 **색인**과 같음. 특정 열로 빠르게 찾게 해줌
```sql
CREATE INDEX idx_orders_customer ON orders(customer_id);
```
- 장점: `WHERE`, `JOIN`에서 조회 속도 ↑
- 비용: 저장공간 ↑, INSERT/UPDATE 시 갱신 부담 ↑ → **자주 조회하는 열에 선별적으로**
- `EXPLAIN QUERY PLAN <쿼리>` 로 인덱스 사용 여부를 확인 (모듈 후반/졸업생 트랙에서 심화)

---

## 🛠 실습 / 산출물
`exercises/`에서 분석형 SQL을 작성합니다.
- HAVING으로 그룹 필터, 서브쿼리로 전체 평균 비교, CASE로 등급 분류, 고객별 합계 등
- `queries.py`를 채우면 `check.py`가 실제 DB에 실행해 정답과 비교
- 산출물: `check.py`를 통과하는 `queries.py`

---

## ✅ 완료 기준 (체크리스트)
- [ ] WHERE와 HAVING의 차이를 설명하고 둘 다 쓸 수 있다
- [ ] 스칼라/IN/FROM 서브쿼리를 작성할 수 있다
- [ ] CASE WHEN으로 조건부 분류를 할 수 있다
- [ ] NULL을 IS NULL/COALESCE로 안전하게 다룬다
- [ ] 인덱스가 무엇이고 왜/언제 쓰는지 설명할 수 있다
- [ ] `exercises/`의 `queries.py`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 집계/서브쿼리/CASE/인덱스 시연 (`schema.sql`, `demo.py`)
- `exercises/starter/` — 채워야 할 쿼리 골격 + 자가 검증
- `exercises/solution/` — 정답 쿼리
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [SQLBolt — 12~18장 (집계/서브쿼리)](https://sqlbolt.com/)
- [Use The Index, Luke! — 인덱스 입문](https://use-the-index-luke.com/)
- 모듈 11(Docker로 Postgres 띄우기)로 이어집니다. (SQLite → 실무 DB)
