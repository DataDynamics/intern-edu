"""pipeline.py 핵심 정제·분석 로직 검증."""
from pipeline import load, clean, revenue_by_category, payment_counts


def main():
    df = clean(load())

    # 정제 결과 검증
    assert len(df) == 11, f"정제 후 11행이어야 합니다(중복1·결측2 제거): {len(df)}"
    assert df["amount"].isna().sum() == 0, "amount에 결측이 남아 있습니다"
    assert str(df["amount"].dtype).startswith("int"), "amount는 정수형이어야 합니다"
    assert set(df["category"].unique()) == {"book", "food", "toy"}, \
        f"category가 소문자로 통일되어야 합니다: {sorted(df['category'].unique())}"

    # 분석 결과 검증
    rev = revenue_by_category(df)
    assert rev == {"book": 67000, "food": 17500, "toy": 50000}, rev
    assert int(df["amount"].sum()) == 134500, df["amount"].sum()
    assert payment_counts(df) == {"card": 7, "cash": 4}, payment_counts(df)

    print("✅ 모든 테스트 통과! (정제 11행, 총매출 134,500)")


if __name__ == "__main__":
    main()
