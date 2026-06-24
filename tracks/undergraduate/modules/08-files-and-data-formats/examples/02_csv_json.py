"""예제 02 — CSV 읽기 → 가공 → JSON 쓰기
실행: python 02_csv_json.py
"""
import csv
import json
import os

csv_path = "/tmp/people_demo.csv"
json_path = "/tmp/people_demo.json"

# 1) 예제 CSV 만들기
with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows([
        {"name": "홍길동", "age": 22},
        {"name": "김영희", "age": 25},
    ])

# 2) CSV 읽기 (값은 모두 문자열!)
with open(csv_path, "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print("raw rows:", rows)

# 3) age를 int로 변환하며 가공
people = [{"name": r["name"], "age": int(r["age"])} for r in rows]
avg_age = sum(p["age"] for p in people) / len(people)
result = {"people": people, "average_age": avg_age}

# 4) JSON으로 저장 (한글 그대로, 들여쓰기)
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("== 저장된 JSON ==")
with open(json_path, "r", encoding="utf-8") as f:
    print(f.read())

os.remove(csv_path); os.remove(json_path)
