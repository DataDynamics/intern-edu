"""status_stats.py 자가 검증."""
from status_stats import classify, summarize


def main():
    assert classify(200) == "success", "200은 success여야 합니다"
    assert classify(404) == "client_error", "404는 client_error여야 합니다"
    assert classify(500) == "server_error", "500은 server_error여야 합니다"
    assert classify(301) == "other", "301은 other여야 합니다"

    result = summarize([200, 200, 404, 500, 403, 301, 200])
    expected = {"success": 3, "client_error": 2, "server_error": 1, "other": 1}
    assert result == expected, f"기대 {expected}, 실제 {result}"

    print("✅ 모든 테스트 통과!")


if __name__ == "__main__":
    main()
