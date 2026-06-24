# 실습 환경 세팅 (0일차)

두 트랙 모두 학습을 시작하기 전에 아래 환경을 준비합니다.

## 준비 항목
1. **Python** — [python-setup.md](python-setup.md) (uv / venv)
2. **Git & GitHub** — [git-setup.md](git-setup.md)
3. **Docker** — [docker/](docker/) (Postgres 등 실습용 컨테이너)
4. **에디터** — VSCode 권장 (확장: Python, Docker)

## 운영체제
- macOS / Linux / Windows(WSL2 권장) 지원
- Windows 사용자는 WSL2 + Ubuntu 환경을 권장합니다.

## 점검
세팅이 끝나면 아래가 모두 동작해야 합니다.

```bash
python --version
git --version
docker --version
```

> 문제가 생기면 [docs/faq.md](../docs/faq.md)를 확인하세요.
