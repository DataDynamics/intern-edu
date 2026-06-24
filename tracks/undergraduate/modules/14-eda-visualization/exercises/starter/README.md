# 실습 — 주문 데이터 EDA 리포트

`orders.csv`를 탐색적으로 분석하고, 차트와 발견 사실 리포트를 만듭니다.

## 할 일
1. `eda.py`의 TODO를 채웁니다.
   - `category_counts(df)` — 카테고리별 주문 **건수**를 `{category: count}` dict로
   - `revenue_by_category(df)` — 카테고리별 **매출 합계**를 `{category: total}` dict로
   - `amount_stats(df)` — amount의 통계를 `{"min","max","mean"}` dict로 (mean은 float)
   - `save_bar_chart(df, path)` — 카테고리별 매출 막대그래프를 path로 저장
     (matplotlib 미설치면 그냥 넘어가도 OK — check는 분석 함수만 검사)
2. 검증: `python check.py`
3. `FINDINGS.md`에 데이터에서 발견한 사실 **3가지**를 글로 작성합니다.

## 산출물
- `check.py` 통과
- (matplotlib 설치 시) `revenue.png`
- 작성된 `FINDINGS.md`
