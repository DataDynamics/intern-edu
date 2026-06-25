# Pagila — DVD 대여점 (Sakila의 PostgreSQL 포트)

MySQL의 대표 샘플인 **Sakila**를 PostgreSQL에 맞게 옮긴 것이 Pagila입니다. PostgreSQL로 Sakila를 연습하고 싶다면 이 버전을 쓰는 것이 정석입니다. 영화·배우·대여·결제로 이어지는 풍부한 스키마라 **다중 조인과 시계열·파티셔닝 연습**까지 가능합니다.

## 출처 / 라이선스
- **출처**: [devrimgunduz/pagila](https://github.com/devrimgunduz/pagila) (`pagila-schema.sql` + `pagila-data.sql`)
- **라이선스**: 원 Sakila 라이선스 계열(자유 사용). 자세한 내용은 원 저장소 참조
- 원본을 커밋하지 않고 적재 시 내려받습니다(스키마 ~52KB + 데이터 ~3.3MB).

## 규모 / 주요 테이블
- 약 20여 개 테이블, 대여(`rental`) 약 16,000 / 결제(`payment`) 약 16,000
- 핵심 흐름: `film` ↔ `film_actor` ↔ `actor`, `film` → `inventory` → `rental` → `payment`, `customer`/`store`/`staff`, `address` → `city` → `country`
- PostgreSQL 고유 타입(`tsvector`, 파티션 테이블 등)을 포함해 학습 가치가 큽니다

## 적재
```bash
./load.sh          # DB 'pagila' 생성 후 스키마→데이터 적재 (PAGILA_DB로 변경 가능)
psql -d pagila
```

## 연습 아이디어
- 카테고리별 대여 건수 / 매출 (`rental` ⨝ `inventory` ⨝ `film_category` ⨝ `category`)
- 가장 많이 대여된 영화 Top N, 고객별 결제액 순위(윈도우 함수)
- 월별 매출 추이, 연체 분석 (`rental_date` / `return_date` 차이)
