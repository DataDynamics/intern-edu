# 모듈 08 — 퀴즈 정답

1. `None`
2. list: 순서 있고 변경 가능 / dict: 키-값 매핑 / set: 중복 없는 집합(순서 X) / tuple: 변경 불가한 묶음
3. 키가 없을 때 `d["key"]`는 `KeyError`로 죽지만, `d.get("key", 0)`은 기본값 0을 반환해 안전.
4. 실제 데이터에는 빈 값·잘못된 형식이 섞여 있어, 한 건의 오류로 전체 처리가 멈추지 않게 하려고.
5. `[0, 2, 4, 6]`
6. `{'b': 1, 'a': 3, 'n': 2}`
7. `15 6`
8.
   ```python
   words = ["a", "abc", "hello", "hi"]
   long_words = [w for w in words if len(w) >= 3]   # ['abc', 'hello']
   ```
9.
   ```python
   def even_sum(nums):
       return sum(n for n in nums if n % 2 == 0)
   ```
10.
   ```python
   total = 0
   for v in ["1", "2", "x", "4"]:
       try:
           total += int(v)
       except ValueError:
           continue
   print(total)   # 7
   ```
