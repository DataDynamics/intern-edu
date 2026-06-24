"""주문 데이터 분석 — TODO를 채우세요."""


def parse_amount(value):
    """문자열 금액을 int로 변환. 실패하면 None."""
    # TODO: try/except로 int(value) 시도, ValueError/TypeError면 None
    pass


def total_revenue(orders):
    """유효한 금액만 합산한 총매출(int)."""
    total = 0
    # TODO: 각 주문의 amount를 parse_amount로 변환, None이 아니면 total에 더하기
    return total


def revenue_by_category(orders):
    """{카테고리: 합계} 딕셔너리. 잘못된 금액은 제외."""
    result = {}
    # TODO: 카테고리별로 유효 금액을 누적 (dict get 패턴 활용)
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
