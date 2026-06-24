# 정답 해설 — EDA

- `value_counts().to_dict()` 로 범주 빈도
- `groupby().sum().to_dict()` 로 범주별 매출
- 통계는 Series의 `.min()/.max()/.mean()` — 검증을 위해 int/float로 캐스팅
- 차트는 **Agg 백엔드 + savefig** 로 화면 없이 저장, matplotlib 미설치 시 안전하게 건너뜀

핵심은 숫자가 아니라 **해석**입니다. `FINDINGS.md`처럼 "무엇이/어느 정도/그래서"를
글로 적는 연습이 데이터 엔지니어·분석가의 핵심 역량입니다.
