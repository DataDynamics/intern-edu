# 모듈 09 — 파일 & 데이터 포맷

> **포커스**: 파일 입출력, CSV/JSON, 인코딩
> **예상 기간**: 1주
> **선행 모듈**: 08 Python 기초 (2)

데이터 엔지니어링의 시작과 끝은 **파일을 읽고 쓰는 것**입니다. 로그, CSV, JSON은
가장 흔한 데이터 포맷입니다. 이 모듈에서 Python으로 이 파일들을 안전하게 읽고,
가공하고, 다시 저장하는 법을 배웁니다. 인코딩(특히 한글) 문제도 다룹니다.

---

## 🎯 학습 목표
- `with open(...)`으로 파일을 안전하게 읽고 쓴다
- CSV를 `csv` 모듈로 읽어 dict 리스트로 다룬다
- JSON을 `json` 모듈로 읽고 쓴다 (직렬화/역직렬화)
- 인코딩(UTF-8)과 한글 처리 문제를 이해한다
- CSV → 가공 → JSON 같은 간단한 변환 파이프라인을 만든다

---

## 📚 핵심 주제

### 1. 파일 읽고 쓰기 — `with open`
`with`를 쓰면 파일을 자동으로 닫아줘 안전합니다. **인코딩은 항상 명시**하세요.
```python
# 쓰기 ('w': 덮어쓰기, 'a': 이어쓰기)
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("안녕\n")
    f.write("데이터\n")

# 읽기 ('r')
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 전체를 문자열로
with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:            # 한 줄씩 (대용량에 적합)
        print(line.strip())   # strip(): 양끝 공백/개행 제거
```

### 2. CSV 다루기 — `csv` 모듈
```python
import csv

# DictReader: 각 행을 헤더 기준 딕셔너리로 읽음 (가장 편함)
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)       # [{'name': '홍길동', 'age': '22'}, ...]

# DictWriter: 딕셔너리 리스트를 CSV로 저장
rows = [{"name": "A", "score": 90}, {"name": "B", "score": 85}]
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)
```
> ⚠️ CSV로 읽은 값은 **모두 문자열**입니다. 숫자로 쓰려면 `int()`/`float()` 변환 필요.
> ⚠️ 쓸 때 `newline=""`을 빼면 윈도우에서 빈 줄이 생깁니다.

### 3. JSON 다루기 — `json` 모듈
```python
import json

data = {"name": "인턴", "skills": ["python", "sql"]}

# 객체 → 파일 (직렬화)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    # ensure_ascii=False : 한글을 \uXXXX 가 아니라 그대로 저장
    # indent=2 : 사람이 읽기 좋게 들여쓰기

# 파일 → 객체 (역직렬화)
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

# 문자열 ↔ 객체
text = json.dumps(data, ensure_ascii=False)   # 객체 → 문자열
obj = json.loads(text)                         # 문자열 → 객체
```

### 4. 인코딩 (한글이 깨질 때)
- 표준은 **UTF-8**. 항상 `encoding="utf-8"`을 명시하세요.
- 오래된 윈도우 파일은 `cp949`(euc-kr)일 수 있습니다 → `encoding="cp949"`로 읽기.
- 깨진 글자(`�`)가 보이면 인코딩 불일치를 의심하세요.

### 5. 포맷 비교 (언제 무엇을?)

| 포맷 | 장점 | 단점 | 주 용도 |
|------|------|------|---------|
| CSV | 단순, 엑셀 호환, 가벼움 | 타입/중첩 표현 불가 | 표 형태 데이터 |
| JSON | 중첩·타입 표현, API 표준 | CSV보다 큼 | API/설정/구조적 데이터 |
| Parquet | 컬럼형, 압축, 빠름 | 사람이 못 읽음 | 대용량 분석 (모듈 후반) |

---

## 🛠 실습 / 산출물
`exercises/`에서 **CSV → JSON 변환 + 집계** 미니 파이프라인을 만듭니다.
- 주문 CSV(`orders.csv`)를 읽어 딕셔너리 리스트로 변환
- 금액을 숫자로 변환하고 카테고리별 매출을 집계
- 집계 결과를 보기 좋은 JSON으로 저장
- 산출물: `check.py`를 통과하는 `convert.py` + 생성된 `summary.json`

---

## ✅ 완료 기준 (체크리스트)
- [ ] `with open(..., encoding="utf-8")`으로 파일을 읽고 쓸 수 있다
- [ ] `csv.DictReader`로 CSV를 dict 리스트로 읽을 수 있다
- [ ] CSV 값이 문자열임을 알고 숫자로 변환할 수 있다
- [ ] `json.dump`/`json.load`로 JSON을 저장·로드할 수 있다
- [ ] `ensure_ascii=False`가 왜 필요한지 안다
- [ ] `exercises/`의 `convert.py`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 실행 가능한 예제 (파일을 실제로 읽고 씀)
- `exercises/starter/` — 실습 골격(TODO) + 입력 CSV + 자가 검증
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [Python 공식 — csv](https://docs.python.org/ko/3/library/csv.html)
- [Python 공식 — json](https://docs.python.org/ko/3/library/json.html)
- 모듈 10(SQL 기초)·모듈 13(pandas)로 이어집니다. (같은 데이터를 DB/판다스로 다룸)
