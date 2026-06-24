"""eda.py 자가 검증 (분석 함수만 — 차트는 선택)."""
import pandas as pd
from eda import category_counts, revenue_by_category, amount_stats


def main():
    df = pd.read_csv("orders.csv")

    assert category_counts(df) == {"book": 3, "food": 3, "toy": 2}, category_counts(df)
    assert revenue_by_category(df) == {"book": 30000, "food": 22500, "toy": 52000}, revenue_by_category(df)

    stats = amount_stats(df)
    assert stats["min"] == 3000, stats
    assert stats["max"] == 30000, stats
    assert abs(stats["mean"] - 13062.5) < 1e-6, stats

    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
