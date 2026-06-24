"""analysis.py 자가 검증."""
import pandas as pd
from analysis import load_clean_orders, revenue_by_category, top_customer


def main():
    df = load_clean_orders()
    assert df["amount"].isna().sum() == 0, "결측치가 남아 있습니다"
    assert str(df["amount"].dtype).startswith("int"), "amount는 정수형이어야 합니다"
    assert int(df["amount"].sum()) == 101500, df["amount"].sum()

    rev = revenue_by_category(df)
    assert rev == {"book": 27000, "food": 22500, "toy": 52000}, rev

    customers = pd.read_csv("customers.csv")
    assert top_customer(df, customers) == "이영희", top_customer(df, customers)

    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
