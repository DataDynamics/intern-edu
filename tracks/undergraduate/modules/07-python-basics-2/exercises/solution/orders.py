"""주문 데이터 분석 — 정답."""


def parse_amount(value):
    """문자열 금액을 int로 변환. 실패하면 None."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def total_revenue(orders):
    """유효한 금액만 합산한 총매출(int)."""
    total = 0
    for order in orders:
        amount = parse_amount(order.get("amount"))
        if amount is not None:
            total += amount
    return total


def revenue_by_category(orders):
    """{카테고리: 합계} 딕셔너리. 잘못된 금액은 제외."""
    result = {}
    for order in orders:
        amount = parse_amount(order.get("amount"))
        if amount is None:
            continue
        category = order.get("category", "unknown")
        result[category] = result.get(category, 0) + amount
    return result


if __name__ == "__main__":
    sample = [
        {"id": 1, "category": "book", "amount": "12000"},
        {"id": 2, "category": "food", "amount": "8000"},
        {"id": 3, "category": "book", "amount": "abc"},
        {"id": 4, "category": "food", "amount": "5500"},
    ]
    print("총매출:", total_revenue(sample))
    print("카테고리별:", revenue_by_category(sample))
