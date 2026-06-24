"""상태코드 통계기 — 정답."""


def classify(status):
    """상태코드 하나를 카테고리 문자열로 분류한다."""
    if 200 <= status < 300:
        return "success"
    elif 400 <= status < 500:
        return "client_error"
    elif 500 <= status < 600:
        return "server_error"
    else:
        return "other"


def summarize(statuses):
    """상태코드 리스트를 카테고리별 개수 딕셔너리로 집계한다."""
    counts = {"success": 0, "client_error": 0, "server_error": 0, "other": 0}
    for status in statuses:
        category = classify(status)
        counts[category] += 1
    return counts


if __name__ == "__main__":
    sample = [200, 200, 404, 500, 403, 301, 200]
    print(summarize(sample))
