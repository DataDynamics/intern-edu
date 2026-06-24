# 모듈 08 — 퀴즈 정답

1. 블록을 벗어나면 파일을 **자동으로 닫아줘서** 자원 누수/잠금 문제를 막는다.
2. `"r"` 읽기 / `"w"` 새로 쓰기(기존 내용 삭제) / `"a"` 기존 끝에 이어쓰기.
3. **문자열(str)**. 숫자로 쓰려면 `int()`/`float()`로 변환해야 한다.
4. 한글 등 비ASCII를 `\uXXXX`로 이스케이프하지 않고 **사람이 읽을 수 있게 그대로** 저장하려고.
5. **JSON** (CSV는 평면 표, Parquet는 사람이 못 읽음).
6. `a.txt`를 한 줄씩 읽어 양끝 공백/개행을 제거한 문자열 리스트를 만든다.
7. `json.dumps`는 객체를 **문자열**로 반환, `json.dump`는 객체를 **파일 객체에 직접 기록**.
8.
   ```python
   import json
   data = {"name": "인턴", "lang": "ko"}
   with open("out.json", "w", encoding="utf-8") as f:
       json.dump(data, f, ensure_ascii=False)
   ```
9.
   ```python
   import csv
   with open("scores.csv", "r", encoding="utf-8") as f:
       rows = list(csv.DictReader(f))
   scores = [int(r["score"]) for r in rows]
   print(sum(scores) / len(scores))
   ```
10. **인코딩 불일치** (예: cp949 파일을 utf-8로 읽음). 올바른 인코딩을 지정해 다시 읽는다.
