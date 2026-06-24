"""환경 점검 — 정답."""
import platform


def python_version():
    """현재 Python 버전을 '3.x.y' 문자열로 반환."""
    return platform.python_version()


def is_supported(version):
    """'3.x.y'에서 major==3 이고 minor>=10 이면 True."""
    parts = version.split(".")
    major = int(parts[0])
    minor = int(parts[1])
    return major == 3 and minor >= 10


def greet(name):
    """'환경 준비 완료, {name}!' 반환."""
    return f"환경 준비 완료, {name}!"


if __name__ == "__main__":
    v = python_version()
    print("버전:", v, "| 지원:", is_supported(v))
    print(greet("인턴"))
