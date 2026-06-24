"""환경 점검 — TODO를 채우세요."""
import platform


def python_version():
    """현재 Python 버전을 '3.x.y' 문자열로 반환."""
    # TODO: platform.python_version() 반환
    pass


def is_supported(version):
    """'3.x.y'에서 major==3 이고 minor>=10 이면 True."""
    # TODO: version.split(".")로 major/minor를 정수로 만들어 판단
    pass


def greet(name):
    """'환경 준비 완료, {name}!' 반환."""
    # TODO: f-string으로 반환
    pass


if __name__ == "__main__":
    v = python_version()
    print("버전:", v, "| 지원:", is_supported(v))
    print(greet("인턴"))
