# 모듈 14 — 퀴즈 정답

1. 데이터의 분포·결측·이상치·관계를 살펴 형태와 품질을 파악하는 과정. 잘못된 데이터로 잘못된 분석/파이프라인을 만들지 않으려고 **가장 먼저** 한다.
2. count(개수), mean(평균), std(표준편차), min/max, 사분위(25/50/75%) 중 3가지.
3. **이상치(극단값)** 나 한쪽으로 치우친(skewed) 분포를 의심.
4. `plt.savefig("파일.png")` (그리고 헤드리스면 `matplotlib.use("Agg")`).
5. 막대: **범주별 비교**, 히스토그램: **하나의 연속값 분포** 확인.

6. `df["category"].value_counts()`
7.
   ```python
   df["amount"].plot(kind="hist", bins=10)
   ```
8.
   ```python
   import matplotlib
   matplotlib.use("Agg")
   import matplotlib.pyplot as plt
   # ... plot ...
   plt.savefig("chart.png")
   ```
9. `df["amount"].quantile([0.25, 0.5, 0.75])`
10. (예) 소수의 고가 주문이 평균을 끌어올려, 일반적인 주문은 평균보다 낮은(중앙값 10,500) 수준이다.
