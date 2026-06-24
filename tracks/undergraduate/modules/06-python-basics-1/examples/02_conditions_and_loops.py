"""예제 02 — 조건문과 반복문
실행: python 02_conditions_and_loops.py
"""

def classify(status):
    if status >= 500:
        return "서버 에러"
    elif status >= 400:
        return "클라이언트 에러"
    elif status >= 200:
        return "정상"
    return "알 수 없음"

statuses = [200, 200, 404, 500, 403, 200]

print("== 각 상태코드 분류 ==")
for s in statuses:
    print(f"  {s} -> {classify(s)}")

print("== 합계/개수 집계 ==")
total = 0
error_count = 0
for s in statuses:
    total += 1
    if s >= 400:
        error_count += 1
print(f"총 {total}건 중 에러 {error_count}건")

print("== break / continue ==")
for n in range(10):
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print("  홀수:", n)
