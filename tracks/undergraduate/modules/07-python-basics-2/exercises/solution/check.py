"""orders.py 자가 검증."""
from orders import parse_amount, total_revenue, revenue_by_category

SAMPLE = [
    {"id": 1, "category": "book", "amount": "12000"},
    {"id": 2, "category": "food", "amount": "8000"},
    {"id": 3, "category": "book", "amount": "abc"},
    {"id": 4, "category": "food", "amount": "5500"},
]


def main():
    assert parse_amount("100") == 100
    assert parse_amount("abc") is None
    assert parse_amount(None) is None

    assert total_revenue(SAMPLE) == 25500, total_revenue(SAMPLE)

    expected = {"book": 12000, "food": 13500}
    assert revenue_by_category(SAMPLE) == expected, revenue_by_category(SAMPLE)

    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
