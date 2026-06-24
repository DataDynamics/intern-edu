# 모듈 07 — Python 기초 (2)

> **포커스**: 함수, 자료구조(list·dict·set·tuple), 예외처리, 모듈
> **예상 기간**: 1주
> **선행 모듈**: 06 Python 기초 (1)

모듈 06에서 코드의 뼈대(변수·조건·반복)를 익혔다면, 이제 **재사용 가능한 함수**와
**데이터를 담는 자료구조**를 배웁니다. 데이터 엔지니어링에서 가장 많이 쓰는 자료구조는
**리스트(list)** 와 **딕셔너리(dict)** 입니다. 이 둘을 자유자재로 다루는 것이 이 모듈의 핵심입니다.

---

## 🎯 학습 목표
- 함수를 정의하고 인자·반환값·기본값을 사용한다
- list / dict / set / tuple의 차이와 용도를 안다
- dict로 데이터를 집계하고, list로 순회·필터링한다
- `try/except`로 예외를 안전하게 처리한다
- 코드를 모듈로 나누고 `import`로 가져온다

---

## 📚 핵심 주제

### 1. 함수 (재사용의 단위)
```python
def add(a, b):
    return a + b

def greet(name, greeting="안녕"):   # 기본값 인자
    return f"{greeting}, {name}!"

print(add(2, 3))              # 5
print(greet("인턴"))           # 안녕, 인턴!
print(greet("인턴", "환영"))    # 환영, 인턴!
```
- 함수는 **하나의 일**만 하도록 작게 쪼개는 것이 좋습니다.
- `return`이 없으면 `None`을 반환합니다.

### 2. 리스트 (list) — 순서 있는 묶음
```python
nums = [10, 20, 30]
nums.append(40)        # [10,20,30,40] 추가
nums[0]                # 10 (인덱스 접근)
nums[-1]               # 40 (뒤에서 첫번째)
nums[1:3]              # [20, 30] (슬라이싱)
len(nums)              # 4

# 리스트 컴프리헨션 (자주 씀)
squares = [n * n for n in range(5)]        # [0,1,4,9,16]
evens = [n for n in nums if n % 20 == 0]   # 조건 필터링
```

### 3. 딕셔너리 (dict) — 키-값 저장 ⭐
데이터 엔지니어링의 주력 자료구조. 집계·매핑·레코드 표현에 쓰입니다.
```python
user = {"name": "intern", "age": 22}
user["name"]               # "intern"
user["city"] = "Seoul"     # 추가/수정
user.get("phone", "없음")   # 키 없으면 기본값 반환 (KeyError 방지)

for key, value in user.items():
    print(key, value)

# 집계 패턴: 단어/항목 개수 세기
words = ["a", "b", "a", "c", "a"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1     # {'a':3,'b':1,'c':1}
```

### 4. set / tuple
```python
unique = set([1, 1, 2, 3, 3])   # {1, 2, 3} — 중복 제거
point = (37.5, 127.0)           # tuple — 변경 불가(immutable), 좌표/고정쌍에 적합
```

| 자료구조 | 순서 | 변경 | 중복 | 대표 용도 |
|----------|------|------|------|-----------|
| list | O | O | O | 순서 있는 데이터 |
| dict | O(3.7+) | O | 키 unique | 매핑/집계/레코드 |
| set | X | O | X | 중복 제거/집합 연산 |
| tuple | O | X | O | 고정된 묶음 |

### 5. 예외 처리 (try / except)
실제 데이터는 더럽습니다. 빈 값, 잘못된 형식이 섞여 있죠. 프로그램이 죽지 않게 합니다.
```python
def to_int(value):
    try:
        return int(value)
    except ValueError:
        return None        # 변환 실패 시 None

to_int("42")    # 42
to_int("abc")   # None  (죽지 않음)
```

### 6. 모듈 (import)
코드를 파일 단위로 나누고 가져다 씁니다.
```python
# utils.py 의 함수를 다른 파일에서:
from utils import to_int

# 표준 라이브러리
import json, csv
from collections import Counter

Counter(["a", "b", "a"])   # Counter({'a': 2, 'b': 1}) — 집계 한 방에
```

---

## 🛠 실습 / 산출물
`exercises/`에서 **주문 데이터 분석 함수 모음**을 작성합니다.
- 주문 레코드(딕셔너리) 리스트가 주어졌을 때:
  - 총 매출 합계 구하기
  - 카테고리별 매출 집계(dict 반환)
  - 잘못된 레코드(금액이 숫자가 아님)는 예외 처리로 건너뛰기
- 산출물: 자가 검증(`check.py`)을 통과하는 `orders.py`

---

## ✅ 완료 기준 (체크리스트)
- [ ] 함수를 정의하고 기본값 인자를 사용할 수 있다
- [ ] list 슬라이싱과 컴프리헨션을 쓸 수 있다
- [ ] dict로 항목별 개수/합계를 집계할 수 있다 (`get` 패턴)
- [ ] list/dict/set/tuple의 차이를 설명할 수 있다
- [ ] `try/except`로 잘못된 데이터를 안전하게 건너뛸 수 있다
- [ ] `exercises/`의 `orders.py`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 실행 가능한 예제 코드
- `exercises/starter/` — 실습 골격(TODO) + 자가 검증 스크립트
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [점프 투 파이썬 — 자료형/함수](https://wikidocs.net/book/1)
- [Python 공식 — 자료구조](https://docs.python.org/ko/3/tutorial/datastructures.html)
- 모듈 08(파일 & 데이터 포맷)로 이어집니다. (여기서 만든 함수로 실제 파일을 처리)
