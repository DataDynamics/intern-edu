# 모듈 12 — 퀴즈 정답

1. DataFrame은 2차원 표(여러 열), Series는 1차원(한 열/배열).
2. `df["amount"]`는 **Series**, `df[["amount"]]`는 (열 1개짜리) **DataFrame**.
3. `GROUP BY ... SUM()`.
4. `inner`는 양쪽 키가 매칭되는 행만, `left`는 왼쪽 전부 + 매칭 없으면 오른쪽은 NaN.
5. 숫자로 변환 불가한 값을 **NaN**으로 만든다(에러를 내지 않음).

6. `df[df["amount"] >= 10000]`
7. `df.groupby("category")["amount"].mean()`
8. `df["amount"] = df["amount"].fillna(0)`
9. `df.sort_values("amount", ascending=False).head(3)`
10. `df[df["category"].isin(["book", "toy"])]`
