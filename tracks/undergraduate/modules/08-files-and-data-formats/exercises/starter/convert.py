"""CSV → 집계 → JSON 변환 — TODO를 채우세요."""
import csv
import json


def load_orders(path):
    """CSV 파일을 읽어 dict 리스트로 반환한다."""
    # TODO: with open + csv.DictReader 로 읽어 list로 반환
    pass


def summarize(orders):
    """{카테고리: 매출합계}. amount가 숫자가 아니면 건너뛴다."""
    result = {}
    # TODO: 각 주문의 amount를 int로 변환(try/except), 성공 시 카테고리별 누적
    return result


def save_json(data, path):
    """dict를 JSON 파일로 저장한다 (한글 그대로, 들여쓰기 2)."""
    # TODO: with open + json.dump(ensure_ascii=False, indent=2)
    pass


if __name__ == "__main__":
    orders = load_orders("orders.csv")
    summary = summarize(orders)
    save_json(summary, "summary.json")
    print("저장 완료:", summary)
