"""예제 — pandas EDA + matplotlib 차트 저장
실행: python demo.py  (pandas 필요, matplotlib 있으면 차트도 저장)
"""
import pandas as pd

df = pd.read_csv("orders.csv")

print("== shape ==", df.shape)
print("\n== describe (amount) ==")
print(df["amount"].describe())
print("\n== category 빈도 ==")
print(df["category"].value_counts())
print("\n== 카테고리별 매출 ==")
rev = df.groupby("category")["amount"].sum().sort_values(ascending=False)
print(rev)

# matplotlib는 선택 — 없으면 건너뜀 (분석은 위에서 끝)
try:
    import matplotlib
    matplotlib.use("Agg")            # 화면 없이 파일로
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    rev.plot(kind="bar", color="steelblue")
    plt.title("Revenue by Category")
    plt.ylabel("amount")
    plt.tight_layout()
    plt.savefig("revenue.png")
    print("\n[차트 저장됨] revenue.png")
except ImportError:
    print("\n[matplotlib 미설치] 분석만 수행. `uv pip install matplotlib` 후 차트 저장 가능")
