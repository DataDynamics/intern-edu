"""예제 02 — 예외 처리와 모듈
실행: python 02_exceptions_and_modules.py
"""
import json


def to_float(value):
    """숫자로 못 바꾸면 None 반환 (프로그램이 죽지 않음)."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


raw = ["19.9", "abc", "", "42", None]
cleaned = [to_float(v) for v in raw]
print("cleaned:", cleaned)               # [19.9, None, None, 42.0, None]

valid = [v for v in cleaned if v is not None]
print("valid sum:", sum(valid))          # 61.9

# 표준 라이브러리 json 사용
record = {"name": "intern", "scores": [90, 85]}
text = json.dumps(record, ensure_ascii=False)
print("json:", text)
print("parsed back:", json.loads(text))
