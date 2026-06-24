# 모듈 07 — Python 기초 (1)

> **포커스**: 변수·자료형, 연산, 조건문, 반복문
> **예상 기간**: 1주
> **선행 모듈**: 03 개발 환경, 05 Linux

Python은 데이터 엔지니어의 **주력 언어**입니다. 데이터를 읽고, 가공하고, 파이프라인을
짜는 거의 모든 일을 Python으로 합니다. 이 모듈은 프로그래밍이 처음인 사람을 기준으로
**변수 → 자료형 → 조건문 → 반복문**까지, 모든 코드의 뼈대가 되는 문법을 다룹니다.

> 💡 실습 전 `python --version`으로 Python 3.10+ 가 설치됐는지 확인하세요. (모듈 03 참고)

---

## 🎯 학습 목표
- 변수에 값을 저장하고 기본 자료형(int, float, str, bool)을 구분한다
- 산술·비교·논리 연산자를 사용한다
- `if / elif / else`로 분기 처리를 작성한다
- `for`, `while` 반복문으로 데이터를 순회·집계한다
- 문자열을 다루고 포맷팅(f-string)한다

---

## 📚 핵심 주제

### 1. 변수와 자료형
```python
count = 10            # int (정수)
price = 19.9          # float (실수)
name = "intern"       # str (문자열)
is_active = True      # bool (참/거짓)

print(type(count))    # <class 'int'>
```
- 변수 이름은 의미 있게 (`x` 보다 `row_count`)
- `type(값)` 으로 자료형 확인, 형 변환은 `int("3")`, `str(3)`, `float("3.5")`

### 2. 연산자
```python
# 산술
1 + 2, 10 - 3, 4 * 5, 10 / 3, 10 // 3, 10 % 3, 2 ** 3
#                       3.33   3(몫)   1(나머지) 8(거듭제곱)

# 비교 (결과는 bool)
3 > 2, 3 == 3, 3 != 4

# 논리
True and False, True or False, not True
```

### 3. 문자열 다루기
```python
s = "Data Engineer"
len(s)                 # 13 (길이)
s.upper()              # "DATA ENGINEER"
s.lower()              # "data engineer"
s.split()              # ['Data', 'Engineer']
"a,b,c".split(",")     # ['a', 'b', 'c']
s.replace("Data", "ML")# "ML Engineer"

# f-string 포맷팅 (가장 많이 씀)
name, n = "logs", 42
print(f"{name} 파일에서 {n}건 처리")   # logs 파일에서 42건 처리
```

### 4. 조건문 (if / elif / else)
들여쓰기(보통 공백 4칸)가 **문법의 일부**입니다.
```python
status = 404

if status >= 500:
    print("서버 에러")
elif status >= 400:
    print("클라이언트 에러")
elif status >= 200:
    print("정상")
else:
    print("알 수 없음")
```

### 5. 반복문 (for / while)
```python
# for: 순회
for i in range(5):          # 0,1,2,3,4
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 집계 패턴 (데이터 처리의 기본)
numbers = [10, 20, 30]
total = 0
for n in numbers:
    total += n              # total = total + n
print(total)               # 60

# while: 조건이 참인 동안
n = 3
while n > 0:
    print(n)
    n -= 1                  # 3,2,1
```

### 6. 흐름 제어: break / continue
```python
for n in range(10):
    if n == 5:
        break              # 반복 즉시 종료
    if n % 2 == 0:
        continue           # 이번 회차 건너뛰기
    print(n)               # 1, 3
```

---

## 🛠 실습 / 산출물
`exercises/`에서 **상태코드 통계기**를 작성합니다.
- 상태코드 리스트가 주어지면, 각 코드가 정상/클라이언트에러/서버에러 중 무엇인지 분류하고
  카테고리별 개수를 세어 출력하는 함수를 완성합니다. (조건문 + 반복문 종합)
- 산출물: 테스트를 통과하는 `status_stats.py`

---

## ✅ 완료 기준 (체크리스트)
- [ ] 네 가지 기본 자료형을 구분하고 형 변환을 할 수 있다
- [ ] f-string으로 문자열을 포맷팅할 수 있다
- [ ] `if/elif/else`로 다중 분기를 작성할 수 있다
- [ ] `for`로 리스트를 순회하며 합계/개수를 집계할 수 있다
- [ ] `break`/`continue`의 차이를 설명할 수 있다
- [ ] `exercises/`의 `status_stats.py`가 검증 스크립트를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 실행 가능한 예제 코드
- `exercises/starter/` — 실습 골격(TODO) + 자가 검증 스크립트
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [점프 투 파이썬 (무료)](https://wikidocs.net/book/1)
- [Python 공식 튜토리얼(한국어)](https://docs.python.org/ko/3/tutorial/)
- 모듈 08(Python 기초 2 — 함수·자료구조)로 이어집니다.
