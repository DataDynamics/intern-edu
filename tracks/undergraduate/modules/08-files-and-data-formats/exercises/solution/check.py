"""convert.py 자가 검증."""
import json
import os
from convert import load_orders, summarize, save_json


def main():
    orders = load_orders("orders.csv")
    assert len(orders) == 6, f"6개 행이어야 합니다: {len(orders)}"
    assert orders[0]["category"] == "book"

    summary = summarize(orders)
    expected = {"book": 15000, "food": 13500, "toy": 15000}
    assert summary == expected, f"기대 {expected}, 실제 {summary}"

    save_json(summary, "summary.json")
    assert os.path.exists("summary.json"), "summary.json이 생성되어야 합니다"
    with open("summary.json", "r", encoding="utf-8") as f:
        loaded = json.load(f)
    assert loaded == expected, "저장된 JSON 내용이 일치해야 합니다"

    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
