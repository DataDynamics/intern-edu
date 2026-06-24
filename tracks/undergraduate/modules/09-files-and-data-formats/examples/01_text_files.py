"""예제 01 — 텍스트 파일 읽고 쓰기 (with open)
실행: python 01_text_files.py
"""
import os

path = "/tmp/hello_demo.txt"

with open(path, "w", encoding="utf-8") as f:
    f.write("안녕\n")
    f.write("데이터 엔지니어\n")

print("== read() 전체 ==")
with open(path, "r", encoding="utf-8") as f:
    print(f.read())

print("== 한 줄씩 ==")
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        print("  ->", line.strip())

os.remove(path)
