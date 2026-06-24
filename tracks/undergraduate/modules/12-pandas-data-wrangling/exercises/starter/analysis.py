"""pandas 주문 분석 — TODO를 채우세요."""
import pandas as pd


def load_clean_orders(path="orders.csv"):
    """orders.csv를 읽고 amount를 정수로 정제(결측/오류는 0)."""
    df = pd.read_csv(path)
    # TODO: amount를 pd.to_numeric(errors="coerce")로 변환,
    #       fillna(0) 후 astype(int)
    return df


def revenue_by_category(df):
    """{category: 매출합계} 딕셔너리 반환."""
    # TODO: groupby("category")["amount"].sum() 후 .to_dict()
    pass


def top_customer(df, customers):
    """총 주문액이 가장 큰 고객의 이름(str) 반환."""
    # TODO: df를 customers와 merge(customer_id ↔ id),
    #       이름별 amount 합계 후 최댓값의 이름 반환
    pass


if __name__ == "__main__":
    orders = load_clean_orders()
    customers = pd.read_csv("customers.csv")
    print("카테고리별:", revenue_by_category(orders))
    print("최대 고객:", top_customer(orders, customers))
