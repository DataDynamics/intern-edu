"""예제 01 — 변수, 자료형, 연산자
실행: python 01_types_and_operators.py
"""

count = 10
price = 19.9
name = "intern"
is_active = True

print("count:", count, type(count))
print("price:", price, type(price))
print("name:", name, type(name))
print("is_active:", is_active, type(is_active))

# 산술
print("10 // 3 =", 10 // 3, "(몫)")
print("10 % 3  =", 10 % 3, "(나머지)")
print("2 ** 3  =", 2 ** 3, "(거듭제곱)")

# 형 변환
print('int("3") + 4 =', int("3") + 4)
print("f-string:", f"{name} 사용자, 잔액 {price}원")
