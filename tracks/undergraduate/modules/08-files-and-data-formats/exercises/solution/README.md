# 정답 해설 — CSV → JSON 변환

## 흐름
`load_orders`(읽기) → `summarize`(가공/집계) → `save_json`(쓰기)로 **단계를 함수로 분리**.
이것이 ETL(Extract-Transform-Load)의 축소판입니다. 모듈 05(졸업생 트랙 ETL)와 직접 연결됩니다.

## 주의 포인트
- CSV 값은 문자열 → `int(order["amount"])`로 변환, 실패 시 `continue`로 건너뜀
- `json.dump`에 `ensure_ascii=False`를 줘야 한글이 `\uXXXX`가 아닌 그대로 저장됨
- `indent=2`로 사람이 읽기 좋게

## 한 걸음 더
- 건너뛴(잘못된) 행 수를 함께 세서 로그로 출력하기
- 결과에 총매출(`total`)도 추가하기
