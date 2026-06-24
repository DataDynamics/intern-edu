# 정답 해설 — SQL 쿼리

| 질문 | 핵심 |
|------|------|
| Q1 | 열 선택 `SELECT name, city` |
| Q2 | `WHERE amount >= 10000` |
| Q3 | `ORDER BY amount DESC LIMIT 3` (정렬 후 상위 N) |
| Q4 | 문자열 비교 `WHERE city = 'Seoul'` |
| Q5 | `JOIN ... ON o.customer_id = c.id` + 별칭 `o`, `c` |
| Q6 | `GROUP BY category` + 집계 `SUM(amount) AS total` |

## 자주 하는 실수
- 문자열 값은 작은따옴표: `'Seoul'` (큰따옴표 X)
- JOIN 시 어느 열로 연결되는지(`ON`)를 빠뜨리면 모든 행이 곱해짐(카티전 곱)
- GROUP BY 없이 집계 함수만 쓰면 전체가 한 그룹으로 묶임

## 한 걸음 더
- Q6에 `COUNT(*) AS cnt`를 추가해 주문 수도 같이 구해보기
- 도시별 고객 수를 GROUP BY로 구해보기
