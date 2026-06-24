"""주문 데이터 EDA — 정답."""
import pandas as pd


def category_counts(df):
    """{category: 주문 건수} 반환."""
    return df["category"].value_counts().to_dict()


def revenue_by_category(df):
    """{category: 매출 합계} 반환."""
    return df.groupby("category")["amount"].sum().to_dict()


def amount_stats(df):
    """{'min','max','mean'} 반환 (mean은 float)."""
    s = df["amount"]
    return {"min": int(s.min()), "max": int(s.max()), "mean": float(s.mean())}


def save_bar_chart(df, path="revenue.png"):
    """카테고리별 매출 막대그래프를 저장 (matplotlib 없으면 건너뜀)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib 미설치 — 차트 생략")
        return
    rev = df.groupby("category")["amount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(6, 4))
    rev.plot(kind="bar", color="steelblue")
    plt.title("Revenue by Category")
    plt.ylabel("amount")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()


if __name__ == "__main__":
    df = pd.read_csv("orders.csv")
    print("건수:", category_counts(df))
    print("매출:", revenue_by_category(df))
    print("통계:", amount_stats(df))
    save_bar_chart(df)
