"""미니 프로젝트 — 판매 데이터 정제·분석 파이프라인 (참고 구현)."""
import json
import pandas as pd


def load(path="sales_raw.csv"):
    """원본 CSV를 DataFrame으로 읽는다."""
    return pd.read_csv(path)


def clean(df):
    """더러운 데이터를 정제한다.

    - 문자열 열 앞뒤 공백 제거
    - category, payment 소문자 통일
    - amount를 숫자로 변환(불가→NaN), NaN 행 제거
    - 완전 중복 행 제거
    """
    df = df.copy()
    for col in ["category", "product", "payment"]:
        df[col] = df[col].astype("string").str.strip()
    df["category"] = df["category"].str.lower()
    df["payment"] = df["payment"].str.lower()

    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])          # 금액 없는/잘못된 행 제거
    df["amount"] = df["amount"].astype(int)

    df = df.drop_duplicates()                  # 완전 중복 제거
    df = df.reset_index(drop=True)
    return df


def revenue_by_category(df):
    return df.groupby("category")["amount"].sum().to_dict()


def revenue_by_date(df):
    return df.groupby("date")["amount"].sum().to_dict()


def payment_counts(df):
    return df["payment"].value_counts().to_dict()


def save_outputs(df, json_path="summary.json", chart_path="revenue_by_category.png"):
    summary = {
        "rows": int(len(df)),
        "total_revenue": int(df["amount"].sum()),
        "revenue_by_category": revenue_by_category(df),
        "revenue_by_date": revenue_by_date(df),
        "payment_counts": payment_counts(df),
    }
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        rev = df.groupby("category")["amount"].sum().sort_values(ascending=False)
        plt.figure(figsize=(6, 4))
        rev.plot(kind="bar", color="steelblue")
        plt.title("Revenue by Category")
        plt.ylabel("amount")
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()
    except ImportError:
        pass
    return summary


if __name__ == "__main__":
    df = clean(load())
    summary = save_outputs(df)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
