"""예제 01 — 함수와 자료구조 (list/dict/set/tuple)
실행: python 01_functions_and_structures.py
"""
from collections import Counter


def summarize(nums):
    """리스트의 합/평균/최댓값을 dict로 반환."""
    return {"sum": sum(nums), "avg": sum(nums) / len(nums), "max": max(nums)}


nums = [10, 20, 30, 40]
print("summary:", summarize(nums))

# 리스트 컴프리헨션
print("squares:", [n * n for n in range(5)])
print("evens:", [n for n in nums if n % 20 == 0])

# dict 집계
words = ["a", "b", "a", "c", "a"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print("counts:", counts)
print("Counter:", dict(Counter(words)))   # 같은 결과를 한 줄로

# set / tuple
print("unique:", set([1, 1, 2, 3, 3]))
print("tuple:", (37.5, 127.0))
