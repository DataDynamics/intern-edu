"""CSV → 집계 → JSON 변환 — 정답."""
import csv
import json


def load_orders(path):
    """CSV 파일을 읽어 dict 리스트로 반환한다."""
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def summarize(orders):
    """{카테고리: 매출합계}. amount가 숫자가 아니면 건너뛴다."""
    result = {}
    for order in orders:
        try:
            amount = int(order["amount"])
        except (ValueError, TypeError):
            continue
        category = order["category"]
        result[category] = result.get(category, 0) + amount
    return result


def save_json(data, path):
    """dict를 JSON 파일로 저장한다 (한글 그대로, 들여쓰기 2)."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    orders = load_orders("orders.csv")
    summary = summarize(orders)
    save_json(summary, "summary.json")
    print("저장 완료:", summary)
