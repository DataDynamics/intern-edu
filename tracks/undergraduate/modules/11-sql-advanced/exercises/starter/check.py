"""queries.py를 실제 PostgreSQL DB에 실행해 정답과 비교.

사전 준비:
  1. PostgreSQL 실행 (설치는 setup/postgresql-setup.md 참고)
  2. pip install psycopg2-binary

접속 정보는 환경변수로 바꿀 수 있습니다.
  - DATABASE_URL=postgresql://사용자:비밀번호@localhost:5432/DB이름
  - 또는 PGHOST/PGPORT/PGUSER/PGPASSWORD/PGDATABASE
  - 아무것도 없으면 libpq 기본값(현재 OS 사용자)으로 접속합니다.
"""
import os
import psycopg2
import queries


def make_conn():
    conn = psycopg2.connect(os.environ.get("DATABASE_URL", ""))
    conn.autocommit = True
    with conn.cursor() as cur, open("schema.sql", "r", encoding="utf-8") as f:
        cur.execute(f.read())
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
    conn = make_conn()
    for key in ["Q1", "Q2", "Q3", "Q4", "Q5"]:
        sql = getattr(queries, key)
        assert sql.strip(), f"{key}가 비어 있습니다"
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        assert rows == EXPECTED[key], f"{key} 결과 불일치:\n  실제   {rows}\n  기대   {EXPECTED[key]}"
        print(f"  {key} 통과")
    conn.close()
    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
