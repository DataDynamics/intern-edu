"""예제 — pandas로 필터/집계/병합/결측치
실행: python demo.py  (pandas 필요: uv pip install pandas)
"""
import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

print("== head & shape ==")
print(orders.head(3))
print("shape:", orders.shape)

print("\n== 결측치 개수 ==")
print(orders.isna().sum())

print("\n== amount 결측을 0으로 채우고 정수화 ==")
orders["amount"] = orders["amount"].fillna(0).astype(int)
print(orders[["id", "category", "amount"]].to_string(index=False))

print("\n== 필터: 1만원 이상 ==")
print(orders[orders["amount"] >= 10000][["id", "amount"]].to_string(index=False))

print("\n== groupby: 카테고리별 합계 ==")
print(orders.groupby("category")["amount"].sum().sort_values(ascending=False))

print("\n== merge: 주문 + 고객이름 ==")
merged = orders.merge(customers, left_on="customer_id", right_on="id",
                      suffixes=("_order", "_customer"))
print(merged[["id_order", "name", "category", "amount"]].head().to_string(index=False))
