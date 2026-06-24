"""queries.py를 실제 SQLite DB에 실행해 정답과 비교."""
import sqlite3
import queries


def make_db():
    conn = sqlite3.connect(":memory:")
    with open("schema.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    return conn


EXPECTED = {
    "Q1": [("book", 3), ("food", 3)],
    "Q2": [(3, 15000), (4, 30000), (7, 22000)],
    "Q3": [(1, "mid"), (2, "low"), (3, "mid"), (4, "high"),
           (5, "low"), (6, "low"), (7, "high"), (8, "low")],
    "Q4": [("이영희", 45000), ("김철수", 42000)],
    "Q5": [(1,), (2,), (5,), (6,), (7,)],
}


def main():
    conn = make_db()
    for key in ["Q1", "Q2", "Q3", "Q4", "Q5"]:
        sql = getattr(queries, key)
        assert sql.strip(), f"{key}가 비어 있습니다"
        rows = list(conn.execute(sql))
        assert rows == EXPECTED[key], f"{key} 결과 불일치:\n  실제   {rows}\n  기대   {EXPECTED[key]}"
        print(f"  {key} 통과")
    conn.close()
    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
