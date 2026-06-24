# Python 환경 세팅

## uv 설치 (권장)
빠른 Python 패키지/가상환경 관리 도구입니다.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 프로젝트 가상환경
```bash
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

> TODO: 표준 requirements 목록 확정 (pandas, matplotlib, jupyter 등)
