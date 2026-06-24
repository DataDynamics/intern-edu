# 모듈 14 — EDA & 시각화 기초

> **포커스**: 탐색적 데이터 분석(EDA), matplotlib 기본 차트
> **예상 기간**: 1주
> **선행 모듈**: 13 pandas

데이터를 받으면 가장 먼저 하는 일은 **"이 데이터가 어떻게 생겼는지 살펴보는 것"**,
즉 EDA(Exploratory Data Analysis)입니다. 분포·이상치·결측·관계를 파악하고, 차트로
한눈에 보이게 만듭니다. 데이터 엔지니어가 파이프라인을 짜기 전, 데이터의 형태와 품질을
이해하는 필수 단계입니다.

> 💡 설치: `uv pip install pandas matplotlib`. 이 모듈의 분석은 pandas로, 그림은 matplotlib로.

---

## 🎯 학습 목표
- 요약 통계(`describe`)와 분포(`value_counts`)로 데이터를 파악한다
- 결측치·이상치를 탐지한다
- matplotlib로 막대/히스토그램/선 그래프를 그린다
- 차트를 파일로 저장하고 해석을 글로 정리한다
- EDA 결과를 바탕으로 "이 데이터로 무엇을 할 수 있는지" 판단한다

---

## 📚 핵심 주제

### 1. EDA의 첫 질문들
데이터를 받으면 스스로 물어봅니다.
- 행/열은 몇 개인가? (`df.shape`)
- 각 열의 타입과 결측은? (`df.info()`, `df.isna().sum()`)
- 숫자 열의 분포는? (`df.describe()` — 평균/최소/최대/사분위)
- 범주형 열의 빈도는? (`df["category"].value_counts()`)
- 이상치(너무 크거나 작은 값)는 없는가?

```python
import pandas as pd
df = pd.read_csv("orders.csv")

df.describe()                      # 숫자 요약 통계
df["category"].value_counts()      # 범주별 개수
df["amount"].quantile([0.25, 0.5, 0.75])   # 사분위수
```

### 2. matplotlib 기본
```python
import matplotlib.pyplot as plt

# 막대그래프: 카테고리별 합계
rev = df.groupby("category")["amount"].sum()
plt.figure(figsize=(6, 4))
rev.plot(kind="bar")
plt.title("Revenue by Category")
plt.ylabel("amount")
plt.tight_layout()
plt.savefig("revenue.png")   # 파일로 저장 (서버/노트북 모두 안전)
```

차트 종류와 용도:
| 차트 | 메서드 | 용도 |
|------|--------|------|
| 막대(bar) | `kind="bar"` | 범주별 비교 |
| 히스토그램 | `df["amount"].plot(kind="hist", bins=10)` | 분포 확인 |
| 선(line) | `kind="line"` | 시간/순서에 따른 추이 |
| 산점도 | `df.plot(kind="scatter", x=..., y=...)` | 두 변수 관계 |

### 3. 차트를 "저장"하는 습관
- 서버나 자동화 환경에는 화면이 없으므로 `plt.show()` 대신 **`plt.savefig("파일.png")`** 로 저장
- 헤드리스 환경에서는 백엔드를 Agg로:
  ```python
  import matplotlib
  matplotlib.use("Agg")   # 화면 없이 파일로만 출력
  ```

### 4. 해석이 핵심
차트는 수단입니다. **"그래서 무엇을 알 수 있는가"** 를 글로 정리하는 것이 EDA의 결과물입니다.
> 예: "toy 카테고리가 매출의 절반을 차지한다. 주문 수는 적지만 객단가가 높다."

### 5. 한글 폰트 (선택)
matplotlib는 기본 폰트에 한글이 없어 `□`로 깨질 수 있습니다. 라벨은 영문으로 쓰거나
시스템 한글 폰트를 지정합니다. (실습에서는 영문 라벨 권장)

---

## 🛠 실습 / 산출물
`exercises/`에서 주문 데이터의 EDA 리포트를 만듭니다.
- 요약 통계/카테고리 빈도/카테고리별 매출을 계산하는 함수 완성 (`check.py`로 검증)
- 카테고리별 매출 막대그래프를 `revenue.png`로 저장 (matplotlib 설치 시)
- `FINDINGS.md`에 "데이터에서 발견한 사실 3가지"를 글로 작성
- 산출물: `check.py` 통과 + `revenue.png` + `FINDINGS.md`

---

## ✅ 완료 기준 (체크리스트)
- [ ] `describe`/`value_counts`로 데이터를 요약할 수 있다
- [ ] 결측치/이상치를 탐지할 수 있다
- [ ] matplotlib로 막대/히스토그램을 그려 파일로 저장할 수 있다
- [ ] 차트에서 읽은 사실을 글(FINDINGS.md)로 정리했다
- [ ] `exercises/`의 `eda.py`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — pandas EDA + matplotlib 차트 저장 예제
- `exercises/starter/` — 분석 골격(TODO) + 입력 CSV + 자가 검증 + FINDINGS 템플릿
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [matplotlib — Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [pandas — Visualization](https://pandas.pydata.org/docs/user_guide/visualization.html)
- 모듈 15(미니 프로젝트)에서 수집→정제→분석→**시각화·발표**로 종합합니다.
