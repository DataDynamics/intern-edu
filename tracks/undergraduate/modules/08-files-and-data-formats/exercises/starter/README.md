# 실습 — CSV → JSON 변환 파이프라인

`orders.csv`(주문 데이터)를 읽어 카테고리별 매출을 집계하고 `summary.json`으로 저장합니다.
모듈 07의 데이터 처리 + 모듈 08의 파일 입출력을 합친 미니 파이프라인입니다.

## 입력: orders.csv
```
id,category,amount
1,book,12000
...
3,book,abc      <- 잘못된 금액 (건너뛰어야 함)
```

## 할 일 — `convert.py`의 TODO를 채우세요
1. `load_orders(path)` — CSV를 읽어 dict 리스트로 반환 (`csv.DictReader`)
2. `summarize(orders)` — `{카테고리: 합계}` 반환. amount가 숫자가 아니면 건너뛰기
3. `save_json(data, path)` — dict를 JSON 파일로 저장 (`ensure_ascii=False, indent=2`)
4. main에서 위 셋을 연결해 `summary.json`을 만든다

## 검증
```bash
python check.py
```
통과하면 `summary.json`도 함께 생성됩니다. 파일을 열어 한글/숫자가 잘 들어갔는지 확인하세요.
