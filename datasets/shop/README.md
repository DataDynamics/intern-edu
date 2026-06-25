# shop — 합성 e-커머스 샘플 (오프라인)

모듈 10·11의 `customers`/`orders` 예제를 **4개 테이블**로 확장한 작은 합성 데이터셋입니다.
인터넷 없이 바로 쓸 수 있도록 CSV를 함께 커밋해 두었습니다. JOIN·집계·서브쿼리·윈도우 함수·날짜 처리까지 두루 연습하기 좋습니다.

## 출처 / 라이선스
- **출처**: 이 저장소에서 생성한 합성 데이터 (`generate.py`, 시드 고정 → 재현 가능)
- **라이선스**: 자유 사용 (실제 인물·거래와 무관)

## 스키마

```mermaid
erDiagram
    CUSTOMERS ||--o{ ORDERS : "주문한다"
    ORDERS ||--o{ ORDER_ITEMS : "포함한다"
    PRODUCTS ||--o{ ORDER_ITEMS : "담긴다"
    CUSTOMERS { int id PK; text name; text city; date signup_date }
    PRODUCTS  { int id PK; text name; text category; int price }
    ORDERS    { int id PK; int customer_id FK; date order_date; text status }
    ORDER_ITEMS { int id PK; int order_id FK; int product_id FK; int quantity; int unit_price }
```

| 테이블 | 행 수 | 설명 |
|--------|------|------|
| `customers` | 15 | 고객 (이름·도시·가입일) |
| `products` | 12 | 상품 (이름·카테고리·가격) |
| `orders` | 44 | 주문 (고객·주문일·상태) |
| `order_items` | 86 | 주문 상세 라인 (주문·상품·수량·단가) |

- `status`: `paid` / `shipped` / `delivered` / `cancelled`
- `category`: `book` / `food` / `toy` / `electronics` / `clothing`
- 금액 합계는 `order_items.quantity * unit_price` 로 계산합니다(주문 시점 단가를 스냅샷).

## 적재

PostgreSQL이 실행 중이어야 합니다 → [../../setup/postgresql-setup.md](../../setup/postgresql-setup.md)

```bash
# 1) 스크립트로 한 번에 (DB 'shop' 생성 + 적재)
./load.sh

# 2) 또는 이미 만든 DB에 직접
psql -d 원하는DB -f load.sql
```

## 연습 아이디어
- 카테고리별 매출 합계 (`order_items` ⨝ `products`, `GROUP BY category`)
- 고객별 총 구매액 Top 5 (`JOIN` + `GROUP BY` + `ORDER BY ... LIMIT`)
- 취소(`cancelled`) 주문 제외 매출 (행 조건 `WHERE` + 그룹 조건 `HAVING`)
- 월별 주문 추이 (`date_trunc('month', order_date)`)
- 고객별 누적 구매액 (윈도우 함수 `SUM() OVER (PARTITION BY ...)`)

## 데이터 재생성
```bash
python generate.py   # CSV 4개를 다시 생성 (시드 고정이라 결과 동일)
```
