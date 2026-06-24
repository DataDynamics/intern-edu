# 실습 — 상태코드 통계기

웹 서버 상태코드 리스트를 받아 카테고리별 개수를 세는 함수를 완성하세요.
조건문과 반복문을 종합적으로 사용하는 연습입니다.

## 할 일
`status_stats.py`의 두 함수에서 `# TODO`를 채웁니다.
1. `classify(status)` — 상태코드 하나를 받아 카테고리 문자열을 반환
   - 200~299 → `"success"`
   - 400~499 → `"client_error"`
   - 500~599 → `"server_error"`
   - 그 외 → `"other"`
2. `summarize(statuses)` — 상태코드 리스트를 받아
   `{"success": n, "client_error": n, "server_error": n, "other": n}` 형태로 개수 반환

## 검증
```bash
python check.py
```
`✅ 모든 테스트 통과!` 가 나오면 성공입니다.

> 정답은 `../solution/status_stats.py` 참고 (먼저 스스로!).
