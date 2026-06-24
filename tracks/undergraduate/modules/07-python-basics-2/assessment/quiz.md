# 모듈 07 — 퀴즈 (Python 기초 2)

## 개념
1. 함수에서 `return`이 없으면 무엇이 반환되나요?
2. list, dict, set, tuple의 핵심 차이를 한 줄씩 쓰세요.
3. `d.get("key", 0)` 이 `d["key"]` 보다 안전한 이유는?
4. `try/except`는 데이터 처리에서 왜 중요한가요?
5. 리스트 컴프리헨션 `[n*2 for n in range(4)]` 의 결과는?

## 코드 읽기
6. 출력은?
   ```python
   counts = {}
   for c in "banana":
       counts[c] = counts.get(c, 0) + 1
   print(counts)
   ```
7. 출력은?
   ```python
   def f(x, y=10):
       return x + y
   print(f(5), f(5, 1))
   ```

## 코드 작성
8. 문자열 리스트에서 길이가 3 이상인 것만 모은 새 리스트를 컴프리헨션으로 만드세요.
9. 정수 리스트를 받아 **짝수만의 합**을 반환하는 함수 `even_sum(nums)`를 작성하세요.
10. `["1", "2", "x", "4"]` 에서 숫자로 변환 가능한 것만 int로 바꿔 합을 구하세요. (예외 처리 사용)
