# 모듈 09 — 파일 & 데이터 포맷

> **포커스**: 파일 입출력, CSV/JSON, 인코딩
> **예상 기간**: 1주
> **선행 모듈**: 08 Python 기초 (2)

데이터 엔지니어링의 시작과 끝은 결국 **파일을 읽고 쓰는 일**입니다. 어딘가에서 데이터를 파일로 받아 와 읽고, 가공한 결과를 다시 파일로 저장하지요. 그래서 파일을 안전하게 다루는 능력은 모든 데이터 작업의 토대가 됩니다. 이 모듈에서는 가장 흔히 만나는 두 포맷인 **CSV**와 **JSON**을 중심으로, Python으로 파일을 읽고 가공하고 저장하는 법을 배웁니다. 그리고 한글 데이터에서 자주 말썽을 부리는 **인코딩** 문제도 함께 다룹니다.

---

## 🎯 이 모듈을 마치면

`with open`으로 파일을 안전하게 읽고 쓰며, CSV를 딕셔너리의 목록으로 다루고, JSON을 저장·로드하며, 인코딩(특히 UTF-8과 한글) 문제를 이해하고, "CSV를 읽어 가공한 뒤 JSON으로 저장"하는 작은 변환 파이프라인을 만들 수 있게 됩니다.

---

## 📚 본문

### 파일을 안전하게 열기 — with open

Python에서 파일을 다루는 정석은 `with open(...)` 구문입니다. `with`로 열면, 작업이 끝나거나 도중에 오류가 나도 파일이 **자동으로 닫혀** 자원이 새거나 잠기는 사고를 막아 줍니다. 파일을 열 때는 모드를 함께 정하는데, 읽기는 `"r"`, 새로 쓰기(기존 내용 삭제)는 `"w"`, 이어 쓰기는 `"a"`입니다. 그리고 **인코딩은 항상 명시**하는 습관을 들이세요. 이 한 가지가 한글 깨짐의 절반을 예방합니다.

```python
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("안녕\n")

with open("hello.txt", "r", encoding="utf-8") as f:
    for line in f:               # 한 줄씩 읽기 (대용량에 적합)
        print(line.strip())      # strip(): 양끝 공백·개행 제거
```

큰 파일을 다룰 때는 `read()`로 통째로 메모리에 올리기보다, 위처럼 한 줄씩 순회하는 편이 안전합니다. 수백만 줄짜리 로그를 다룰 일이 생기면 이 차이가 중요해집니다.

### CSV — 표 형태 데이터의 대표 주자

쉼표로 칸을 나눈 CSV는 가장 널리 쓰이는 데이터 포맷입니다. Python의 `csv` 모듈, 그중에서도 `DictReader`를 쓰면 각 행을 헤더 이름을 키로 하는 딕셔너리로 읽어 주어 다루기가 편합니다.

```python
import csv

with open("data.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))   # [{'name': '홍길동', 'age': '22'}, ...]
```

여기서 입문자가 반드시 기억해야 할 함정이 둘 있습니다. 첫째, **CSV에서 읽은 값은 전부 문자열**입니다. 숫자처럼 보여도 계산하려면 `int()`나 `float()`로 변환해야 합니다. 둘째, CSV로 **쓸 때**는 `newline=""` 옵션을 줘야 윈도우에서 줄 사이에 빈 줄이 끼는 문제를 피할 수 있습니다.

```python
rows = [{"name": "A", "score": 90}]
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(rows)
```

### JSON — 구조가 있는 데이터의 언어

CSV가 평평한 표라면, JSON은 목록 안에 객체가 들어가는 식의 **중첩 구조**를 표현할 수 있습니다. API가 주고받는 데이터, 설정 파일이 대부분 JSON이지요. Python의 `json` 모듈로 객체를 파일에 쓰고(`dump`), 파일에서 객체로 읽습니다(`load`).

```python
import json

data = {"name": "인턴", "skills": ["python", "sql"]}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
```

여기서 `ensure_ascii=False`가 핵심입니다. 이 옵션을 빼면 한글이 `인턴`처럼 알아볼 수 없는 코드로 저장됩니다. 사람이 읽을 수 있게 한글을 그대로 두려면 반드시 `ensure_ascii=False`를 주고, 보기 좋게 들여쓰려면 `indent=2`를 더합니다. 문자열과 객체를 직접 변환하는 `json.dumps`(객체→문자열)와 `json.loads`(문자열→객체)도 함께 알아 두면 좋습니다.

### 인코딩 — 글자가 깨질 때

인코딩은 글자를 컴퓨터가 저장하는 숫자로 바꾸는 약속입니다. 오늘날의 표준은 **UTF-8**이며, 우리는 항상 `encoding="utf-8"`을 명시합니다. 그런데 오래된 윈도우에서 만든 파일은 `cp949`(euc-kr) 인코딩일 수 있어서, UTF-8로 읽으면 한글이 `�`처럼 깨져 보입니다. 화면에 이런 깨진 글자가 보인다면 가장 먼저 인코딩 불일치를 의심하고, `encoding="cp949"`로 다시 읽어 보세요.

### 어떤 포맷을 언제 쓰나

| 포맷 | 장점 | 한계 | 주 용도 |
|------|------|------|---------|
| CSV | 단순·가벼움, 엑셀 호환 | 타입·중첩 표현 불가 | 표 형태 데이터 |
| JSON | 중첩·타입 표현, API 표준 | CSV보다 큼 | API·설정·구조적 데이터 |
| Parquet | 컬럼형·압축·빠름 | 사람이 못 읽음 | 대용량 분석 |

지금은 CSV와 JSON에 집중하지만, 데이터가 커지면 **Parquet** 같은 전용 포맷이 등장한다는 것 정도는 알아 두세요. 포맷마다 강점이 다르므로, 상황에 맞게 고르는 것도 데이터 엔지니어의 판단입니다.

---

## 🛠 실습으로 익히기

`exercises/`에서 **CSV를 읽어 집계한 뒤 JSON으로 저장하는** 작은 파이프라인을 만듭니다. 주문 CSV를 딕셔너리 목록으로 읽고, 금액을 숫자로 바꾸되 불량 값은 건너뛰며, 카테고리별 매출을 집계해 보기 좋은 JSON으로 저장하는 것이 과제입니다. 이것은 사실 "추출→변환→적재"라는 ETL의 축소판으로, 졸업생 트랙에서 본격적으로 다루는 파이프라인의 씨앗입니다. `python check.py`가 통과하면 완성입니다.

---

## ✅ 완료 기준 (체크리스트)
- [ ] `with open(..., encoding="utf-8")`으로 파일을 읽고 쓸 수 있다
- [ ] `csv.DictReader`로 CSV를 딕셔너리 목록으로 읽을 수 있다
- [ ] CSV 값이 문자열임을 알고 숫자로 변환할 수 있다
- [ ] `json.dump`/`json.load`로 JSON을 저장·로드할 수 있다
- [ ] `ensure_ascii=False`가 왜 필요한지 안다
- [ ] 인코딩 깨짐의 원인을 진단할 수 있다
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
- 다음 모듈 10(SQL 기초)·13(pandas)에서 같은 데이터를 DB와 판다스로 다룹니다.
