# 모듈 06 — Git & 협업

> **포커스**: commit / 브랜치 / PR, GitHub 협업
> **예상 기간**: 1주
> **선행 모듈**: 05 Linux 기초

데이터 엔지니어는 혼자 일하지 않습니다. 파이프라인 코드, SQL, 설정을 **여럿이 함께**
고치고, 누가 무엇을 왜 바꿨는지 추적해야 합니다. Git은 그 모든 변경 이력을 관리하는
표준 도구이고, GitHub는 그것을 팀과 공유·리뷰하는 공간입니다. 이 모듈에서 우리 교육
저장소에 **실제로 PR을 올리는 것**까지 경험합니다.

---

## 🎯 학습 목표
- Git이 무엇을 해결하는지(버전 관리·협업) 설명한다
- `add → commit → push`의 기본 흐름을 자유롭게 수행한다
- 브랜치를 만들고 작업한 뒤 main에 **Pull Request(PR)** 로 병합한다
- 좋은 커밋 메시지를 작성하고, 변경 이력을 조회한다
- 충돌(conflict)이 왜 생기고 어떻게 해결하는지 이해한다

---

## 📚 핵심 주제

### 1. Git이 푸는 문제
- "최종_진짜최종_v3.py" 같은 파일명 지옥 → **버전 이력**으로 해결
- 여러 명이 같은 파일을 동시에 수정 → **브랜치 + 병합**으로 해결
- "이거 누가 왜 바꿨지?" → **커밋 메시지 + blame**으로 추적

### 2. 3개의 공간 (꼭 이해하기)
```
작업 디렉토리  --git add-->  스테이징(Staging)  --git commit-->  로컬 저장소  --git push-->  원격(GitHub)
 (수정 중)                    (커밋할 후보)                       (이력 저장)                 (팀 공유)
```

### 3. 기본 흐름
```bash
git status                 # 현재 상태 확인 (가장 자주 쓰는 명령)
git add file.py            # 파일을 스테이징
git add .                  # 변경된 것 전부 스테이징
git commit -m "메시지"      # 스테이징된 것을 커밋
git push                   # 원격으로 업로드
git log --oneline          # 커밋 이력 한 줄로 보기
git diff                   # 아직 스테이징 안 된 변경 보기
```

### 4. 브랜치 & PR (협업의 핵심)
`main`에 직접 푸시하지 않습니다. **브랜치를 따서 작업 → PR로 리뷰 → 병합**합니다.

```bash
git switch -c feature/add-report   # 새 브랜치 생성 + 이동 (구버전: git checkout -b)
# ... 코드 수정 ...
git add .
git commit -m "Add weekly report script"
git push -u origin feature/add-report
```
이후 GitHub에서 **Pull Request**를 열어 리뷰를 받고, 승인되면 `main`에 병합합니다.

```bash
git switch main            # main으로 돌아오기
git pull                   # 병합된 최신 main 받아오기
```

### 5. 좋은 커밋 메시지
- 첫 줄은 **무엇을 했는지** 50자 내외로 요약 (명령형: "Add", "Fix", "Update")
- 필요하면 빈 줄 뒤에 **왜** 그렇게 했는지 본문 작성
```
Fix incorrect status-code parsing in log analyzer

awk was reading the wrong field index after the log format
changed. Use $9 consistently.
```

### 6. 충돌(Conflict)
두 사람이 같은 줄을 다르게 고치면 병합 시 충돌이 납니다. Git이 표시한
`<<<<<<<`, `=======`, `>>>>>>>` 구역에서 **올바른 내용만 남기고** 마커를 지운 뒤
다시 `add → commit` 하면 해결됩니다. (당황하지 말 것!)

### 7. 자주 쓰는 구조 도구
```bash
git clone <url>            # 원격 저장소 복제
git restore file.py        # 수정 취소 (커밋 전)
git switch -                # 직전 브랜치로 토글
.gitignore                 # 추적하지 않을 파일 패턴 (예: .venv/, .env)
```

---

## 🛠 실습 / 산출물
1. 교육 저장소를 fork/clone 한다.
2. `feature/<본인이름>-intro` 브랜치를 만든다.
3. `exercises/`의 안내에 따라 `students/<본인이름>.md` 자기소개 파일을 추가한다.
4. commit → push → **Pull Request**를 연다.
5. 산출물: 머지된(또는 리뷰 받은) PR 링크 + 자기소개 파일

---

## ✅ 완료 기준 (체크리스트)
- [ ] Git의 3개 공간(작업/스테이징/저장소)을 설명할 수 있다
- [ ] `add → commit → push`를 막힘없이 수행한다
- [ ] 브랜치를 만들어 작업하고 main에 PR을 올렸다
- [ ] 명령형으로 의미 있는 커밋 메시지를 작성했다
- [ ] `git log --oneline`으로 이력을 조회할 수 있다
- [ ] 충돌이 무엇인지, 해결 절차를 설명할 수 있다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 명령어 흐름 따라하기 데모 스크립트
- `exercises/starter/` — PR 실습 안내 + 자기소개 템플릿
- `exercises/solution/` — 작성 예시
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [Pro Git (무료 한국어 책)](https://git-scm.com/book/ko/v2)
- [GitHub Docs — Hello World](https://docs.github.com/ko/get-started/quickstart/hello-world)
- [Oh Sh*t, Git!?!](https://ohshitgit.com/ko) — 망쳤을 때 복구법
- 모듈 05(Linux), 모듈 07(Python 기초)와 이어집니다.
