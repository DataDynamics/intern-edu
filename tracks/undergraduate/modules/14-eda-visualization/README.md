# 모듈 14 — EDA & 시각화 기초

> **포커스**: 탐색적 데이터 분석(EDA), matplotlib 기본 차트
> **예상 기간**: 1주
> **선행 모듈**: 13 pandas

> 📖 **처음 보는 용어가 있나요?** 이 과정에서 쓰는 핵심 용어는 [용어집](../../../glossary.md)에 정리해 두었습니다. 막히는 단어가 나오면 먼저 찾아보세요.

낯선 데이터를 받았을 때 가장 먼저 해야 할 일은, 곧장 분석에 뛰어드는 것이 아니라 **"이 데이터가 대체 어떻게 생겼는지 살펴보는 것"**입니다. 이 과정을 **탐색적 데이터 분석(EDA, Exploratory Data Analysis)**이라 부릅니다. 분포는 어떤지, 빠진 값은 없는지, 이상한 값은 없는지, 항목들이 서로 어떤 관계인지를 파악하고, 그것을 차트로 한눈에 보이게 만드는 단계지요. 데이터 엔지니어가 파이프라인을 짜기 전에 데이터의 형태와 품질을 이해하는, 빠뜨릴 수 없는 과정입니다.

설치는 `uv pip install pandas matplotlib`로 합니다. 분석은 pandas로 하고, 그림은 matplotlib로 그립니다.

---

## 🎯 이 모듈을 마치면

요약 통계와 빈도로 데이터의 윤곽을 파악하고, 결측치·이상치를 짚어 내며, matplotlib로 막대·히스토그램 같은 기본 차트를 그려 파일로 저장하고, 무엇보다 차트에서 읽어 낸 사실을 **글로 정리**할 수 있게 됩니다.

---

## 📚 본문

### EDA — 데이터에 던지는 첫 질문들

데이터를 받으면 스스로 몇 가지를 물어봅니다. 행과 열은 몇 개인가(`df.shape`), 각 열의 타입과 빠진 값은 어떤가(`df.info()`, `df.isna().sum()`), 숫자 열의 분포는 어떤가(`df.describe()`), 범주형 열에는 어떤 값이 얼마나 자주 나오는가(`value_counts()`). 이 질문들에 답하다 보면 데이터의 윤곽이 잡힙니다.

EDA는 대체로 다음과 같은 흐름으로 진행됩니다.

```mermaid
flowchart LR
    A["데이터 받기"] --> B["살펴보기<br/>shape · describe · value_counts"]
    B --> C["결측·이상치 점검"]
    C --> D["차트로 시각화"]
    D --> E["해석을 글로 정리"]
```

```python
import pandas as pd
df = pd.read_csv("orders.csv")

df.describe()                      # 평균·최소·최대·사분위 등 요약
df["category"].value_counts()      # 범주별 개수
df["amount"].quantile([0.25, 0.5, 0.75])   # 사분위수
```

특히 `describe`가 주는 평균과 중앙값(50%)을 비교하는 습관이 중요합니다. 둘이 크게 다르면, 소수의 극단값(이상치)이 평균을 끌어당기고 있다는 신호일 수 있습니다.

### matplotlib — 숫자를 그림으로

표 속의 숫자는 차트로 바꾸면 훨씬 빨리 와닿습니다. matplotlib로 그림을 그리는 흐름은 단순합니다. 데이터를 준비하고, 차트 종류를 정해 그리고, 제목과 축 이름을 붙인 뒤, **파일로 저장**합니다.

```python
import matplotlib
matplotlib.use("Agg")              # 화면 없는 환경에서도 파일로 출력
import matplotlib.pyplot as plt

rev = df.groupby("category")["amount"].sum()
rev.plot(kind="bar")
plt.title("Revenue by Category")
plt.tight_layout()
plt.savefig("revenue.png")         # 화면에 띄우지 않고 파일로
```

차트 종류는 목적에 따라 고릅니다. 범주별 비교에는 **막대(bar)**, 한 값의 분포 확인에는 **히스토그램**, 시간에 따른 추이에는 **선(line)**, 두 변수의 관계에는 **산점도(scatter)**가 어울립니다. 한 가지 실무 습관을 강조하자면, 서버나 자동화 환경에는 화면이 없으므로 `plt.show()`로 띄우는 대신 **`plt.savefig()`로 파일에 저장**하는 방식이 안전합니다. 위 코드의 `matplotlib.use("Agg")`가 바로 그 화면 없는 환경을 위한 설정입니다.

### 해석이 진짜 결과물이다

여기서 가장 중요한 이야기를 해야겠습니다. 차트는 목적이 아니라 **수단**입니다. EDA의 진짜 결과물은 예쁜 그래프가 아니라, "그래서 무엇을 알 수 있는가"라는 **해석**입니다. 예컨대 "toy 카테고리가 매출의 절반을 차지한다. 주문 건수는 적지만 객단가가 높기 때문이다" 같은 한 문장이, 차트 열 장보다 값집니다. 숫자와 그림에서 의미를 읽어 내 말과 글로 풀어내는 능력 — 이것이 AI 시대에도 사람의 몫으로 남는, 데이터를 다루는 사람의 핵심 역량입니다.

> 💡 한글 라벨은 matplotlib 기본 폰트에서 깨질 수 있습니다. 실습에서는 차트 라벨을 영문으로 쓰거나 시스템 한글 폰트를 지정하세요.

---

## 🛠 실습으로 익히기

`exercises/`에서 주문 데이터의 EDA 리포트를 만듭니다. 요약 통계와 카테고리 빈도, 카테고리별 매출을 계산하는 함수를 완성하고(`check.py`로 검증), 카테고리별 매출 막대그래프를 저장하며, 무엇보다 `FINDINGS.md`에 **데이터에서 발견한 사실 세 가지**를 글로 적습니다. matplotlib가 없으면 분석 함수만으로도 검증은 통과하도록 설계되어 있으니, 환경에 구애받지 말고 진행하세요.

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
- 다음 모듈 15(미니 프로젝트)에서 수집→정제→분석→시각화→발표를 한데 종합합니다.
