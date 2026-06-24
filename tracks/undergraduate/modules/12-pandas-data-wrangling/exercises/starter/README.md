# 실습 — pandas로 주문 데이터 분석

주문/고객 CSV를 pandas로 정제·집계·병합하는 함수를 완성합니다.
(09~10에서 SQL로 풀던 문제를 이번엔 pandas로!)

## 데이터
- `orders.csv` : id, customer_id, category, amount (amount에 빈 값=결측 1건 존재)
- `customers.csv` : id, name, city

## 할 일 — `analysis.py`의 TODO를 채우세요
1. `load_clean_orders()` — orders.csv를 읽고 `amount`를 숫자로 변환,
   결측/변환불가는 0으로 채운 뒤 정수형(int)으로. 정제된 DataFrame 반환
2. `revenue_by_category(df)` — 카테고리별 매출 합계를
   `{category: total}` **딕셔너리**로 반환
3. `top_customer(df, customers)` — 주문과 고객을 merge해
   **총 주문액이 가장 큰 고객의 이름(str)** 반환

## 검증
```bash
python check.py
```
