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
    "Q1": [("김철수", "Seoul"), ("이영희", "Busan"), ("박민수", "Seoul"), ("최지우", "Incheon")],
    "Q2": [(1, 12000), (3, 15000), (4, 30000), (7, 22000)],
    "Q3": [(4, 30000), (7, 22000), (3, 15000)],
    "Q4": [("김철수",), ("박민수",)],
    "Q5": [
        (1, "김철수", 12000), (2, "김철수", 8000), (3, "이영희", 15000),
        (4, "이영희", 30000), (5, "박민수", 5500), (6, "박민수", 3000),
        (7, "김철수", 22000), (8, "최지우", 9000),
    ],
    "Q6": [("toy", 52000), ("book", 30000), ("food", 22500)],
}

# 순서를 따지지 않아도 되는 쿼리 (집합 비교)
UNORDERED = {"Q1", "Q2", "Q4"}


def main():
    conn = make_conn()
    for key in ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6"]:
        sql = getattr(queries, key)
        assert sql.strip(), f"{key}가 비어 있습니다"
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()
        expected = EXPECTED[key]
        if key in UNORDERED:
            assert sorted(rows) == sorted(expected), f"{key} 결과 불일치: {rows}"
        else:
            assert rows == expected, f"{key} 결과(순서 포함) 불일치: {rows}"
        print(f"  {key} 통과")
    conn.close()
    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
