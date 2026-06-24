# 모듈 12 — 퀴즈 (pandas)

## 개념
1. DataFrame과 Series의 차이는?
2. `df["amount"]` 와 `df[["amount"]]` 의 결과 타입 차이는?
3. pandas의 `groupby().sum()` 은 SQL의 무엇에 해당하나요?
4. `merge`의 `how="inner"` 와 `how="left"` 의 차이는?
5. `pd.to_numeric(s, errors="coerce")` 는 변환 불가 값을 어떻게 처리하나요?

## 코드 작성 (df: id, category, amount 가정)
6. amount가 10000 이상인 행만 남기는 코드를 쓰세요.
7. 카테고리별 평균 amount를 구하는 코드를 쓰세요.
8. amount 결측치를 0으로 채우는 코드를 쓰세요.
9. amount 기준 내림차순으로 상위 3개 행을 보는 코드를 쓰세요.
10. 'book'과 'toy' 카테고리만 남기는 코드를 쓰세요. (`isin` 사용)
