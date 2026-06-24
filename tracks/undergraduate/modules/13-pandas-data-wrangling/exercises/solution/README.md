# 정답 해설 — pandas 분석

| 함수 | 핵심 |
|------|------|
| `load_clean_orders` | `pd.to_numeric(..., errors="coerce")` 로 더러운 값→NaN, `fillna(0).astype(int)` |
| `revenue_by_category` | `groupby("category")["amount"].sum().to_dict()` (SQL GROUP BY 대응) |
| `top_customer` | `merge`(JOIN) → `groupby("name").sum()` → `idxmax()`(최댓값의 인덱스=이름) |

## SQL과 비교
- `groupby().sum()` ≈ `GROUP BY ... SUM()`
- `merge(left_on=, right_on=)` ≈ `JOIN ... ON`
- `idxmax()` ≈ `ORDER BY total DESC LIMIT 1` 의 이름만 뽑기

## 한 걸음 더
- 카테고리별 **평균/건수**도 `.agg(["sum","mean","count"])`로 함께 구하기
- 도시(city)별 매출도 구해보기 (merge 후 groupby("city"))
