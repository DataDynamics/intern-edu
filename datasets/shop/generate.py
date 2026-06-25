"""shop 샘플 데이터 생성기 (재현 가능, 시드 고정).

실행: python generate.py
결과: customers.csv / products.csv / orders.csv / order_items.csv

이 데이터는 모듈 10·11의 customers/orders 예제를 확장한 합성(synthetic) 데이터로,
JOIN·집계·서브쿼리·윈도우 함수·날짜 처리를 두루 연습할 수 있도록 설계했습니다.
실제 인물/거래와 무관하며 자유롭게 사용·수정할 수 있습니다.
"""
import csv
import random
from datetime import date, timedelta

random.seed(42)

CITIES = ["Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju"]
STATUSES = ["paid", "shipped", "delivered", "cancelled"]
STATUS_WEIGHTS = [0.15, 0.20, 0.55, 0.10]

CUSTOMER_NAMES = [
    "김철수", "이영희", "박민수", "최지우", "정해인", "한소희", "오세훈",
    "윤아름", "임도현", "강은별", "신우진", "조하늘", "배수지", "문상철", "권나라",
]

PRODUCTS = [
    # (name, category, price)
    ("파이썬 입문서",      "book",        18000),
    ("데이터 분석 교재",    "book",        27000),
    ("SQL 레시피",         "book",        23000),
    ("초콜릿 선물세트",     "food",        15000),
    ("유기농 원두 1kg",     "food",        29000),
    ("수제 쿠키 박스",      "food",         9000),
    ("블록 장난감",        "toy",         34000),
    ("보드게임 클래식",     "toy",         42000),
    ("무선 이어폰",        "electronics", 89000),
    ("기계식 키보드",       "electronics", 76000),
    ("USB-C 허브",         "electronics", 32000),
    ("코튼 후드티",        "clothing",    39000),
]

START = date(2024, 1, 1)


def rand_date(start, span_days):
    return start + timedelta(days=random.randint(0, span_days))


def main():
    # customers
    customers = []
    for cid, name in enumerate(CUSTOMER_NAMES, start=1):
        signup = rand_date(START, 200)
        customers.append((cid, name, random.choice(CITIES), signup.isoformat()))

    # products
    products = []
    for pid, (name, cat, price) in enumerate(PRODUCTS, start=1):
        products.append((pid, name, cat, price))

    # orders + order_items
    orders = []
    items = []
    oid = 0
    item_id = 0
    for cust in customers:
        cid, _, _, signup = cust
        signup_date = date.fromisoformat(signup)
        n_orders = random.randint(1, 4)
        for _ in range(n_orders):
            oid += 1
            # 주문일은 가입일 이후
            max_span = (date(2024, 12, 31) - signup_date).days
            odate = signup_date + timedelta(days=random.randint(0, max(max_span, 1)))
            status = random.choices(STATUSES, weights=STATUS_WEIGHTS, k=1)[0]
            orders.append((oid, cid, odate.isoformat(), status))
            # 1~3 종류의 상품 라인
            for prod in random.sample(products, k=random.randint(1, 3)):
                item_id += 1
                pid, _, _, price = prod
                qty = random.randint(1, 3)
                items.append((item_id, oid, pid, qty, price))

    def dump(path, header, rows):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(rows)
        print(f"  {path}: {len(rows)}행")

    dump("customers.csv", ["id", "name", "city", "signup_date"], customers)
    dump("products.csv", ["id", "name", "category", "price"], products)
    dump("orders.csv", ["id", "customer_id", "order_date", "status"], orders)
    dump("order_items.csv", ["id", "order_id", "product_id", "quantity", "unit_price"], items)
    print("✅ 생성 완료")


if __name__ == "__main__":
    main()
