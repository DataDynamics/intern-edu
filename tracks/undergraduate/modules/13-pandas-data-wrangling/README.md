# 모듈 13 — pandas로 데이터 다루기

> **포커스**: DataFrame, 필터·정렬·집계·병합(merge), 결측치 처리
> **예상 기간**: 1주
> **선행 모듈**: 08 Python 기초(2), 09 파일/포맷, 10 SQL

표 형태의 데이터를 Python에서 다룰 때, 사실상의 표준 도구가 **pandas**입니다. CSV·엑셀·데이터베이스에서 데이터를 읽어 와 거르고, 묶고, 합치는 일을 SQL보다 더 유연하게, 코드로 자유롭게 해냅니다. 데이터 엔지니어와 분석가가 가장 손에 자주 잡는 도구라 해도 과언이 아닙니다.

재미있는 점은, 여기서 하는 일의 상당수가 앞서 SQL로 하던 것과 똑같다는 것입니다. SQL의 `WHERE`는 pandas의 조건 필터로, `GROUP BY`는 `groupby`로, `JOIN`은 `merge`로 거의 일대일 대응됩니다. 그래서 이 모듈은 "같은 문제를 다른 도구로 푸는" 경험이기도 합니다. 설치는 `uv pip install pandas`로 하고, `import pandas as pd`로 불러오는 것이 관례입니다.

---

## 🎯 이 모듈을 마치면

CSV를 DataFrame으로 읽어 구조를 살피고, 조건으로 행을 거르고, `groupby`로 그룹별 통계를 내고, `merge`로 두 데이터를 병합하며, 결측치(NaN)를 탐지하고 처리할 수 있게 됩니다. SQL로 알던 개념을 pandas로 옮겨 표현하는 감각을 갖추게 됩니다.

---

## 📚 본문

### DataFrame — pandas의 표

pandas의 중심에는 **DataFrame**이 있습니다. 행과 열로 이루어진 표로, 엑셀 시트나 데이터베이스 테이블을 떠올리면 됩니다(열 하나만 떼어 낸 1차원 데이터는 Series라고 부릅니다). CSV를 읽어 들이는 것은 `read_csv` 한 줄이면 되고, 데이터를 받으면 가장 먼저 그 생김새부터 살핍니다.

```python
import pandas as pd
df = pd.read_csv("orders.csv")

df.head()        # 앞 5행 맛보기
df.shape         # (행 수, 열 수)
df.info()        # 열별 타입과 결측 개요
df.describe()    # 숫자 열의 요약 통계
```

데이터를 받자마자 `head`, `shape`, `info`, `describe`로 훑어보는 습관 — 이것이 좋은 데이터 작업의 첫 단추입니다. 다음 모듈(EDA)에서 더 깊이 다루지만, "먼저 들여다본다"는 태도는 여기서부터 시작됩니다.

### 행 고르기 — 불리언 인덱싱

원하는 행만 추리는 것은 SQL의 `WHERE`에 해당합니다. pandas에서는 조건식을 대괄호 안에 넣는 **불리언 인덱싱**으로 표현합니다. 여러 조건을 엮을 때는 `&`(그리고)와 `|`(또는)를 쓰고, 각 조건을 괄호로 감싸야 한다는 점만 주의하면 됩니다.

```python
df[df["amount"] >= 10000]
df[(df["amount"] >= 10000) & (df["category"] == "book")]
df[df["category"].isin(["book", "toy"])]
```

### 정렬과 새 열 만들기

`sort_values`로 정렬하고, 기존 열을 가공해 새 열을 손쉽게 추가할 수 있습니다. pandas의 강력함은 열 전체에 연산이 한 번에 적용된다는 점입니다. `df["amount"] / 1000`이라고 쓰면 모든 행의 금액이 한꺼번에 나뉩니다.

```python
df.sort_values("amount", ascending=False)        # 금액 내림차순
df["amount_k"] = df["amount"] / 1000              # 파생 열 추가
```

### groupby — SQL의 GROUP BY를 pandas로

그룹별 통계는 `groupby`로 냅니다. "카테고리별 매출 합계"는 카테고리로 묶어 금액을 더하면 되지요. SQL의 `GROUP BY category ... SUM(amount)`와 발상이 똑같습니다. 여러 통계를 한 번에 보려면 `agg`로 묶습니다.

```python
df.groupby("category")["amount"].sum()
df.groupby("category")["amount"].agg(["sum", "mean", "count"])
```

### merge — SQL의 JOIN을 pandas로

두 DataFrame을 키로 이어 붙이는 것이 `merge`이며, SQL의 `JOIN`에 해당합니다. 어느 열을 기준으로 이을지(`left_on`, `right_on`), 어떤 방식으로 이을지(`how`: inner/left/right/outer)를 지정합니다.

```python
merged = orders.merge(customers, left_on="customer_id", right_on="id", how="inner")
```

여기까지 보면, SQL을 아는 사람에게 pandas가 한결 친숙하게 느껴질 것입니다. 같은 개념(필터·집계·조인)을 도구만 바꿔 표현하고 있을 뿐이니까요.

### 결측치 — 비어 있는 칸 다루기

현실의 데이터에는 빈 칸이 흔하고, pandas는 이를 `NaN`(Not a Number)으로 표시합니다. 어디에 결측이 있는지 세어 보고, 상황에 맞게 채우거나(`fillna`) 버립니다(`dropna`). 특히 숫자여야 할 열에 글자가 섞여 있을 때 `pd.to_numeric(..., errors="coerce")`를 쓰면, 변환에 실패한 값을 NaN으로 바꿔 줍니다 — 이는 모듈 08에서 배운 `try/except`로 불량 데이터를 건너뛰던 것과 같은 정신입니다.

```python
df.isna().sum()                                              # 열별 결측 개수
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")  # 변환 실패 → NaN
df["amount"] = df["amount"].fillna(0)                        # 결측을 0으로
```

---

## 🛠 실습으로 익히기

`exercises/`에서 주문·고객 CSV를 pandas로 분석합니다. 금액을 숫자로 정제하고(결측 처리 포함), 카테고리별 매출을 집계하고, 주문과 고객을 `merge`해 총 주문액이 가장 큰 고객을 찾는 것이 과제입니다. 09·10에서 풀던 문제를 이번엔 pandas로 다시 푸는 셈이라, 도구 사이의 대응 관계가 자연스럽게 몸에 익습니다. `python check.py`가 통과하면 완성입니다.

---

## ✅ 완료 기준 (체크리스트)
- [ ] CSV를 DataFrame으로 읽고 `head`/`shape`/`describe`로 살펴본다
- [ ] 불리언 인덱싱으로 행을 필터링한다
- [ ] `groupby`로 그룹별 합계/평균/개수를 구한다
- [ ] `merge`로 두 DataFrame을 병합한다
- [ ] 결측치를 탐지하고 처리(`fillna`/`dropna`/`coerce`)한다
- [ ] pandas 작업을 SQL 개념과 연결해 설명할 수 있다
- [ ] `exercises/`의 `analysis.py`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 실행 가능한 pandas 예제 + 샘플 CSV
- `exercises/starter/` — 실습 골격(TODO) + 입력 CSV + 자가 검증
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [pandas 공식 — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [pandas Cheat Sheet (PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- 다음 모듈 14(EDA & 시각화)에서 이 DataFrame을 탐색하고 그림으로 표현합니다.
