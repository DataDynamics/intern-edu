# 정답 해설 — 주문 데이터 분석

## 핵심
- `parse_amount`를 **한 곳**에 두고 나머지 함수가 재사용 → 더러운 데이터 처리 로직이 한 군데로 모임
- `try/except (ValueError, TypeError)` 로 `"abc"`(ValueError)와 `None`(TypeError)을 모두 안전 처리
- 집계는 `result[key] = result.get(key, 0) + amount` 패턴 (키가 없으면 0부터 시작)
- 잘못된 값은 `if amount is None: continue` 로 건너뜀

## 한 걸음 더
- `collections.defaultdict(int)`로 집계 코드를 더 짧게 써보기
- 카테고리별 **평균** 주문액도 구해보기 (개수도 함께 집계)
