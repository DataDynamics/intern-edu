# 모듈 13 — pandas로 데이터 다루기

> **포커스**: DataFrame, 필터·정렬·집계·병합(merge), 결측치 처리
> **예상 기간**: 1주
> **선행 모듈**: 08 Python 기초(2), 09 파일/포맷, 10 SQL

`pandas`는 Python에서 표 형태 데이터를 다루는 **사실상의 표준** 라이브러리입니다.
CSV/Excel/DB에서 데이터를 읽어 필터·집계·병합하는 일을, SQL보다 더 유연하게 코드로
수행합니다. 데이터 엔지니어/분석가의 가장 기본적인 작업 도구입니다.

> 💡 설치: `uv pip install pandas` (모듈 03 환경 참고). `import pandas as pd` 가 관례입니다.
> 09~10에서 SQL로 하던 집계를, 이번엔 pandas로 해보며 **같은 문제·다른 도구**를 경험합니다.

---

## 🎯 학습 목표
- DataFrame/Series의 구조를 이해하고 CSV를 읽어들인다
- 열 선택, 행 필터링(불리언 인덱싱), 정렬을 한다
- `groupby`로 그룹별 집계를 한다 (SQL의 GROUP BY에 대응)
- 두 DataFrame을 `merge`로 병합한다 (SQL의 JOIN에 대응)
- 결측치(NaN)를 탐지하고 처리한다

---

## 📚 핵심 주제

### 1. DataFrame 만들고 살펴보기
```python
import pandas as pd

df = pd.read_csv("orders.csv")     # CSV 읽기 (타입 자동 추론)
df.head()        # 앞 5행
df.shape         # (행수, 열수)
df.columns       # 열 이름
df.dtypes        # 열별 자료형
df.describe()    # 숫자 열 요약 통계 (count/mean/min/max...)
df.info()        # 결측치/타입 개요
```

### 2. 열 선택 & 행 필터링
```python
df["amount"]                 # 한 열 (Series)
df[["category", "amount"]]   # 여러 열 (DataFrame)

# 불리언 인덱싱 (SQL의 WHERE)
df[df["amount"] >= 10000]
df[(df["amount"] >= 10000) & (df["category"] == "book")]   # & and, | or
df[df["category"].isin(["book", "toy"])]
```

### 3. 정렬 & 새 열
```python
df.sort_values("amount", ascending=False)          # 금액 내림차순
df["amount_k"] = df["amount"] / 1000               # 파생 열 추가
df["grade"] = df["amount"].apply(
    lambda x: "high" if x >= 20000 else "low")     # 조건부 열
```

### 4. groupby 집계 ⭐ (SQL GROUP BY 대응)
```python
df.groupby("category")["amount"].sum()             # 카테고리별 합계
df.groupby("category")["amount"].agg(["sum", "mean", "count"])
df.groupby("category").size()                      # 그룹별 행 수

# 보기 좋게 정리
(df.groupby("category")["amount"]
   .sum()
   .sort_values(ascending=False)
   .reset_index(name="total"))
```

### 5. merge — 병합 (SQL JOIN 대응)
```python
customers = pd.read_csv("customers.csv")   # id, name, city
orders = pd.read_csv("orders.csv")         # id, customer_id, ...

merged = orders.merge(customers, left_on="customer_id", right_on="id",
                      how="inner", suffixes=("_order", "_customer"))
# how: "inner"(기본) / "left" / "right" / "outer"
```

### 6. 결측치(NaN) 처리
```python
df.isna().sum()              # 열별 결측 개수
df.dropna()                  # 결측 있는 행 제거
df["amount"].fillna(0)       # 결측을 0으로 채우기
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")  # 변환 실패→NaN
```
> 📌 `errors="coerce"`는 숫자로 못 바꾸는 값(`"abc"`)을 NaN으로 만들어, 더러운 데이터를
> 안전하게 처리하게 해줍니다. (모듈 08의 try/except 패턴과 같은 목적)

---

## 🛠 실습 / 산출물
`exercises/`에서 주문/고객 CSV를 pandas로 분석합니다.
- amount를 숫자로 정제(결측 처리), 조건 필터, 카테고리별 집계, 고객-주문 merge
- `analysis.py`의 함수들을 채우면 `check.py`가 실제 DataFrame으로 검증
- 산출물: `check.py`를 통과하는 `analysis.py`

---

## ✅ 완료 기준 (체크리스트)
- [ ] CSV를 DataFrame으로 읽고 `head`/`shape`/`describe`로 살펴본다
- [ ] 불리언 인덱싱으로 행을 필터링한다
- [ ] `groupby`로 그룹별 합계/평균/개수를 구한다
- [ ] `merge`로 두 DataFrame을 병합한다
- [ ] 결측치를 탐지하고 처리(`fillna`/`dropna`/`coerce`)한다
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
- 모듈 14(EDA & 시각화)로 이어집니다. (여기서 만든 DataFrame을 시각화)
