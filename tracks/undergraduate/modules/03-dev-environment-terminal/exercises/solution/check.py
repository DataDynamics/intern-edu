"""env_check.py 자가 검증."""
import platform
from env_check import python_version, is_supported, greet


def main():
    assert python_version() == platform.python_version()

    assert is_supported("3.10.0") is True
    assert is_supported("3.12.3") is True
    assert is_supported("3.9.18") is False
    assert is_supported("2.7.18") is False

    assert greet("인턴") == "환경 준비 완료, 인턴!", greet("인턴")

    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
