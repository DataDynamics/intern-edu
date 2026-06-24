"""예제 — 내 Python 환경 정보 출력
실행: python env_info.py
"""
import sys
import platform

print("Python 버전:", platform.python_version())
print("실행 파일 경로:", sys.executable)   # .venv 안이면 가상환경 경로가 보임
print("OS:", platform.system(), platform.release())

# 가상환경 안인지 간단 추정
in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
print("가상환경 활성화됨?", "예" if in_venv else "아니오")
