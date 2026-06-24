# 실습 — 주문 데이터 분석 함수 모음

주문 레코드(딕셔너리) 리스트를 분석하는 함수들을 완성합니다.
함수 · dict 집계 · 예외 처리를 종합합니다.

## 데이터 형태
```python
orders = [
    {"id": 1, "category": "book",   "amount": "12000"},
    {"id": 2, "category": "food",   "amount": "8000"},
    {"id": 3, "category": "book",   "amount": "abc"},   # 잘못된 금액!
]
```
`amount`는 문자열이고, 가끔 숫자가 아닌 더러운 값이 섞여 있습니다.

## 할 일 — `orders.py`의 TODO를 채우세요
1. `parse_amount(value)` — 문자열을 int로 변환, 실패하면 `None` 반환 (`try/except`)
2. `total_revenue(orders)` — 유효한 금액만 합산한 총매출 (int)
3. `revenue_by_category(orders)` — `{카테고리: 합계}` dict 반환 (잘못된 금액은 제외)

## 검증
```bash
python check.py
```
`✅ 모든 테스트 통과!` 가 목표입니다.
