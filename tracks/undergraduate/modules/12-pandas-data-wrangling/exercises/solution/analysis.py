"""pandas 주문 분석 — 정답."""
import pandas as pd


def load_clean_orders(path="orders.csv"):
    """orders.csv를 읽고 amount를 정수로 정제(결측/오류는 0)."""
    df = pd.read_csv(path)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0).astype(int)
    return df


def revenue_by_category(df):
    """{category: 매출합계} 딕셔너리 반환."""
    return df.groupby("category")["amount"].sum().to_dict()


def top_customer(df, customers):
    """총 주문액이 가장 큰 고객의 이름(str) 반환."""
    merged = df.merge(customers, left_on="customer_id", right_on="id")
    totals = merged.groupby("name")["amount"].sum()
    return totals.idxmax()


if __name__ == "__main__":
    orders = load_clean_orders()
    customers = pd.read_csv("customers.csv")
    print("카테고리별:", revenue_by_category(orders))
    print("최대 고객:", top_customer(orders, customers))
