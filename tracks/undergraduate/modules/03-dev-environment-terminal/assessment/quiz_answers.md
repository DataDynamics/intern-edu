# 모듈 03 — 퀴즈 정답

1. 터미널은 명령을 입력/출력하는 **창**, 쉘은 그 명령을 **해석·실행**하는 프로그램(bash/zsh).
2. 프로젝트마다 패키지를 **격리**해, 서로 다른 버전이 충돌하지 않게 하려고.
3. 프롬프트 앞에 `(.venv)` 가 보인다. 비활성화는 `deactivate`.
4. 설치한 패키지 목록을 기록해 **다른 사람/다른 컴퓨터에서 동일하게 재현**하기 위해.
5. `python hello.py`는 **파일**을 실행, `python -c "..."`는 **한 줄 코드**를 즉석 실행.

6.
   ```bash
   uv venv
   source .venv/bin/activate
   ```
7. `uv pip install pandas`
8. `uv pip freeze > requirements.txt`
9. `python --version` (또는 `python3 --version`)
10. `code .`
