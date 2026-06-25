# 실습 — 분석형 SQL 작성

09와 같은 고객·주문 DB에 대해 **집계·서브쿼리·CASE**를 사용하는 쿼리를 작성합니다.
`queries.py`의 Q1~Q5를 채우세요.

## 풀어야 할 질문
- **Q1 (HAVING)**: 주문이 **3건 이상**인 카테고리의 `category`, `cnt`(주문수). `category` 오름차순
- **Q2 (서브쿼리)**: **전체 평균 금액보다 비싼** 주문의 `id`, `amount`. `id` 오름차순
- **Q3 (CASE)**: 모든 주문의 `id`와 등급 `grade`
  (amount>=20000 → 'high', >=10000 → 'mid', 그 외 'low'). `id` 오름차순
- **Q4 (JOIN+집계)**: 고객별 총 주문액이 **20000 이상**인 고객의 `name`, `total`. `total` 내림차순
- **Q5 (IN 서브쿼리)**: 'Seoul'에 사는 고객이 낸 주문의 `id`. `id` 오름차순

## 사전 준비
- PostgreSQL이 실행 중이어야 합니다 → [설치 & 접속 세팅](../../../../../../setup/postgresql-setup.md)
- Python 드라이버 설치: `pip install psycopg2-binary`
- 접속 정보는 환경변수로 바꿀 수 있습니다(`DATABASE_URL` 또는 `PG*`). 기본값은 현재 OS 사용자로 접속합니다.

## 검증
```bash
python check.py
```
