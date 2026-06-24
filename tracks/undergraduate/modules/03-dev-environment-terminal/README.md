# 모듈 03 — 개발 환경 & 터미널

> **포커스**: 터미널/쉘, VSCode, Python 환경(uv/venv), 패키지 관리
> **예상 기간**: 1주
> **선행 모듈**: 02 (오리엔테이션)

코드를 한 줄 쓰기 전에, **개발자처럼 일할 수 있는 환경**을 갖춰야 합니다. 터미널을 열고,
에디터를 쓰고, Python 가상환경을 만들어 패키지를 설치하고, 스크립트를 실행하는 것 —
이것이 모든 실습의 출발점입니다. 이 모듈을 마치면 이후 모든 모듈을 진행할 준비가 됩니다.

> 💡 운영체제별: macOS/Linux는 기본 터미널, Windows는 **WSL2 + Ubuntu**를 권장합니다.

---

## 🎯 학습 목표
- 터미널을 열고 기본 명령으로 이동·확인을 한다
- VSCode를 설치하고 폴더를 열어 코드를 편집한다
- `uv`(또는 venv)로 Python 가상환경을 만든다
- 가상환경에 패키지를 설치하고 스크립트를 실행한다
- 가상환경이 왜 필요한지 설명한다

---

## 📚 핵심 주제

### 1. 터미널/쉘이란
- **터미널**: 명령어로 컴퓨터에 일을 시키는 창
- **쉘(shell)**: 명령을 해석하는 프로그램 (bash, zsh)
- 자주 쓰는 첫 명령 (자세한 건 모듈 04에서):
```bash
pwd        # 현재 위치
ls         # 파일 목록
cd 폴더     # 이동
clear      # 화면 지우기
```

### 2. 코드 에디터 — VSCode
- [code.visualstudio.com](https://code.visualstudio.com/) 에서 설치
- 추천 확장: **Python**, **Docker**, (선택) Korean Language Pack
- 폴더 열기: `File > Open Folder` 또는 터미널에서 `code .`
- 통합 터미널: `Ctrl + ~` (백틱)

### 3. Python 설치 확인
```bash
python --version      # 또는 python3 --version
```
3.10 이상이면 OK. 없으면 [python.org](https://www.python.org/) 또는 `uv`로 설치.

### 4. 가상환경 (virtual environment) ⭐
프로젝트마다 **독립된 패키지 공간**을 둡니다. 프로젝트 A와 B가 서로 다른 버전의
라이브러리를 써도 충돌하지 않게 합니다.

**uv 사용 (권장 — 빠름)**
```bash
# uv 설치 (macOS/Linux)
curl -LsSf https://astral.sh/uv/install.sh | sh

uv venv                       # .venv 가상환경 생성
source .venv/bin/activate     # 활성화 (Windows: .venv\Scripts\activate)
uv pip install pandas         # 패키지 설치
```

**기본 venv 사용 (대안)**
```bash
python -m venv .venv
source .venv/bin/activate
pip install pandas
```
- 활성화되면 프롬프트 앞에 `(.venv)`가 보입니다.
- 빠져나오기: `deactivate`

### 5. 스크립트 실행
```bash
python hello.py        # 파일 실행
python -c "print(1+1)" # 한 줄 실행
```

### 6. requirements.txt
설치한 패키지 목록을 파일로 관리해 **남도 똑같이 재현**하게 합니다.
```bash
uv pip freeze > requirements.txt      # 현재 패키지 목록 저장
uv pip install -r requirements.txt    # 목록대로 설치
```

---

## 🛠 실습 / 산출물
1. 가상환경을 만들고 활성화한다.
2. `exercises/`의 `env_check.py`를 완성한다 (환경이 정상인지 스스로 확인하는 스크립트).
3. `python check.py`로 검증한다.
- 산출물: 동작하는 가상환경 + 통과하는 `env_check.py`

---

## ✅ 완료 기준 (체크리스트)
- [ ] 터미널에서 `pwd`/`ls`/`cd`로 이동할 수 있다
- [ ] VSCode로 폴더를 열어 파일을 편집할 수 있다
- [ ] 가상환경을 만들고 활성화/비활성화할 수 있다
- [ ] 가상환경에 패키지를 설치하고 스크립트를 실행했다
- [ ] 가상환경이 왜 필요한지 설명할 수 있다
- [ ] `exercises/`의 `env_check.py`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 환경 점검 예제 스크립트
- `exercises/starter/` — 완성할 스크립트(TODO) + 자가 검증
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [uv 공식 문서](https://docs.astral.sh/uv/)
- [VSCode로 Python 시작하기](https://code.visualstudio.com/docs/python/python-tutorial)
- 모듈 04(Linux 기초)에서 터미널 명령을 본격적으로 다룹니다.
