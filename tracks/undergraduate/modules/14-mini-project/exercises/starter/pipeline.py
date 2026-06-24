"""미니 프로젝트 — 판매 데이터 정제·분석 파이프라인 (TODO를 채우세요).

원본(sales_raw.csv)에는 다음 문제가 섞여 있습니다:
  - 카테고리 대소문자 불일치 (Book/BOOK/book)
  - 앞뒤 공백 ( 데이터중심설계 , 'toy ', ' cash')
  - 금액 결측/형식오류 (빈 값, 'abc')
  - 완전 중복 행
이를 정제한 뒤 분석하세요.
"""
import json
import pandas as pd


def load(path="sales_raw.csv"):
    """원본 CSV를 DataFrame으로 읽는다."""
    # TODO: pd.read_csv
    pass


def clean(df):
    """더러운 데이터를 정제한다.
    - category/product/payment 앞뒤 공백 제거
    - category, payment 소문자 통일
    - amount 숫자 변환(불가→NaN), NaN 행 제거, 정수화
    - 완전 중복 행 제거
    정제된 DataFrame 반환 (인덱스 리셋).
    """
    # TODO: 위 단계를 구현
    pass


def revenue_by_category(df):
    """{category: 매출합계} 반환."""
    # TODO
    pass


def revenue_by_date(df):
    """{date: 매출합계} 반환."""
    # TODO
    pass


def payment_counts(df):
    """{payment: 건수} 반환."""
    # TODO
    pass


def save_outputs(df, json_path="summary.json", chart_path="revenue_by_category.png"):
    """summary.json과 카테고리별 매출 차트를 저장한다."""
    summary = {
        "rows": int(len(df)),
        "total_revenue": int(df["amount"].sum()),
        "revenue_by_category": revenue_by_category(df),
        "revenue_by_date": revenue_by_date(df),
        "payment_counts": payment_counts(df),
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    # 차트는 선택 (matplotlib 설치 시): TODO로 막대그래프 저장 추가 가능
    return summary


if __name__ == "__main__":
    df = clean(load())
    print(json.dumps(save_outputs(df), ensure_ascii=False, indent=2))
