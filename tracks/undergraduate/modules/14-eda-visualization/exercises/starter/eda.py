"""주문 데이터 EDA — TODO를 채우세요."""
import pandas as pd


def category_counts(df):
    """{category: 주문 건수} 반환."""
    # TODO: df["category"].value_counts().to_dict()
    pass


def revenue_by_category(df):
    """{category: 매출 합계} 반환."""
    # TODO: groupby 합계 후 to_dict()
    pass


def amount_stats(df):
    """{'min':..., 'max':..., 'mean':...} 반환 (mean은 float)."""
    # TODO: df["amount"]의 min/max/mean을 dict로
    pass


def save_bar_chart(df, path="revenue.png"):
    """카테고리별 매출 막대그래프를 저장 (matplotlib 없으면 조용히 건너뜀)."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib 미설치 — 차트 생략")
        return
    # TODO: groupby 매출을 막대그래프로 그려 path에 savefig


if __name__ == "__main__":
    df = pd.read_csv("orders.csv")
    print("건수:", category_counts(df))
    print("매출:", revenue_by_category(df))
    print("통계:", amount_stats(df))
    save_bar_chart(df)
