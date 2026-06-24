# 모듈 09 — 퀴즈 (파일 & 데이터 포맷)

## 개념
1. `with open(...)`을 쓰면 무엇이 좋은가요?
2. 파일 모드 `"r"`, `"w"`, `"a"` 의 차이를 쓰세요.
3. `csv.DictReader`로 읽은 값의 자료형은 무엇인가요? 주의할 점은?
4. `json.dump`에서 `ensure_ascii=False`는 왜 필요한가요?
5. CSV / JSON / Parquet 중, 중첩 구조(리스트 안의 객체 등)를 표현하기 좋은 것은?

## 코드 읽기
6. 다음 코드가 하는 일을 한 문장으로 설명하세요.
   ```python
   with open("a.txt", "r", encoding="utf-8") as f:
       lines = [line.strip() for line in f]
   ```
7. `json.dumps`와 `json.dump`의 차이는?

## 코드 작성
8. 딕셔너리 `{"name": "인턴", "lang": "ko"}` 를 `out.json`에 한글 그대로 저장하는 코드를 쓰세요.
9. `scores.csv`(헤더 name,score)를 읽어 score 평균을 구하는 코드를 쓰세요. (값 변환 주의)
10. 한글이 깨져 보일 때(`�`) 가장 먼저 의심할 것은 무엇인가요?
