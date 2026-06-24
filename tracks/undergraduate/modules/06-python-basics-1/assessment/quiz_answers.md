# 모듈 06 — 퀴즈 정답

1. `int`, `float`, `str`, `bool`
2. `10/3 = 3.333...`, `10//3 = 3`(몫), `10%3 = 1`(나머지)
3. 문자열 앞에 `f`를 붙여 `{변수}`를 값으로 끼워넣는 포맷팅. 결과: `"logs.txt"`
4. Python은 들여쓰기로 코드 블록(어디까지가 if에 속하는지)을 구분하기 때문. 들여쓰기가 틀리면 문법 오류 또는 의도와 다른 동작.
5. `break`는 반복문을 즉시 **종료**, `continue`는 현재 회차만 건너뛰고 **다음 회차로** 진행.
6. `6` (2 + 4)
7. `0 0 / 0 1 / 1 0 / 1 1 / 2 0 / 2 1` (총 6줄)
8.
   ```python
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   else:
       print("C")
   ```
9.
   ```python
   nums = [5, 3, 8, 1]
   biggest = nums[0]
   for n in nums:
       if n > biggest:
           biggest = n
   print(biggest)   # 8
   ```
10.
   ```python
   total = 0
   for n in range(1, 101):
       if n % 3 == 0:
           total += n
   print(total)   # 1683
   ```
