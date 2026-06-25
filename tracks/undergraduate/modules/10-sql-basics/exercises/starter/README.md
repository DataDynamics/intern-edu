# 실습 — SQL 쿼리 작성

고객(`customers`)·주문(`orders`) DB에 대해 질문에 답하는 SQL을 작성합니다.
`queries.py`의 각 쿼리 문자열(빈 `""`)을 채우세요.

## 스키마
```
customers(id, name, city)
orders(id, customer_id, category, amount)
```

## 풀어야 할 질문 (queries.py의 Q1~Q6)
- **Q1**: 모든 고객의 `name`, `city`를 조회
- **Q2**: 금액(`amount`)이 10000 이상인 주문의 `id`, `amount` 조회
- **Q3**: 주문을 금액 내림차순으로 정렬해 상위 3건의 `id`, `amount` 조회
- **Q4**: 'Seoul'에 사는 고객의 `name` 조회
- **Q5**: 각 주문의 `주문id`, `고객이름`, `amount`를 JOIN으로 조회 (id 오름차순)
- **Q6**: 카테고리별 매출 합계를 `category`, `total`(별칭)로, 합계 내림차순 조회

## 사전 준비
- PostgreSQL이 실행 중이어야 합니다 → [설치 & 접속 세팅](../../../../../../setup/postgresql-setup.md)
- Python 드라이버 설치: `pip install psycopg2-binary`
- 접속 정보는 환경변수로 바꿀 수 있습니다(`DATABASE_URL` 또는 `PG*`). 기본값은 현재 OS 사용자로 접속합니다.

## 검증
```bash
python check.py
```
`✅ 모든 테스트 통과!` 가 목표입니다. (`check.py`가 `schema.sql`을 DB에 적재한 뒤 쿼리를 실행합니다.)
