# 정답 해설 — 분석형 SQL

| 질문 | 핵심 기법 |
|------|-----------|
| Q1 | `GROUP BY` 후 `HAVING COUNT(*) >= 3` (그룹 필터) |
| Q2 | 스칼라 서브쿼리 `> (SELECT AVG(amount) ...)` |
| Q3 | `CASE WHEN ... THEN ... ELSE ... END` |
| Q4 | JOIN + `GROUP BY` + `HAVING SUM(...) >= 20000` |
| Q5 | `IN (SELECT ...)` 서브쿼리 |

## 포인트
- **WHERE vs HAVING**: Q1·Q4는 "그룹"을 거르므로 HAVING. 개별 행 조건이면 WHERE.
- 서브쿼리는 "먼저 안쪽을 계산한 결과를 바깥에서 사용"으로 읽으면 쉬움.
- CASE의 조건은 **위에서부터** 평가되므로 큰 임계값을 먼저 둠.

## 한 걸음 더
- Q3 결과를 `GROUP BY grade`로 다시 묶어 등급별 개수 구하기
- Q4를 서브쿼리(FROM 절 파생 테이블) 버전으로도 작성해보기
