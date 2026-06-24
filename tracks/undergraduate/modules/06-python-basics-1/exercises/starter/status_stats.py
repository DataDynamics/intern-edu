"""상태코드 통계기 — TODO를 채우세요."""


def classify(status):
    """상태코드 하나를 카테고리 문자열로 분류한다."""
    # TODO: status 범위에 따라 "success"/"client_error"/"server_error"/"other" 반환
    pass


def summarize(statuses):
    """상태코드 리스트를 카테고리별 개수 딕셔너리로 집계한다."""
    counts = {"success": 0, "client_error": 0, "server_error": 0, "other": 0}
    # TODO: statuses를 순회하며 classify로 분류하고 counts를 1씩 증가시키세요
    return counts


if __name__ == "__main__":
    sample = [200, 200, 404, 500, 403, 301, 200]
    print(summarize(sample))
