# 실습 — 첫 Pull Request 올리기

교육 저장소에 **자기소개 파일을 추가하는 PR**을 직접 열어봅니다.
데이터 엔지니어 팀의 실제 협업 흐름을 그대로 따릅니다.

## 단계
1. 저장소를 clone(또는 fork)합니다.
   ```bash
   git clone <저장소_URL>
   cd intern-edu
   ```
2. 작업 브랜치를 만듭니다. (main에 직접 작업하지 않습니다!)
   ```bash
   git switch -c feature/<본인영문이름>-intro
   ```
3. 이 폴더의 `students/` 안에 `<본인영문이름>.md`를 만들고
   `template.md`를 참고해 자기소개를 채웁니다.
4. 커밋합니다. (명령형 메시지!)
   ```bash
   git add tracks/undergraduate/modules/05-git-collaboration/exercises/starter/students/<본인영문이름>.md
   git commit -m "Add intro for <본인영문이름>"
   ```
5. 푸시하고 PR을 엽니다.
   ```bash
   git push -u origin feature/<본인영문이름>-intro
   ```
   GitHub에서 `main`을 대상으로 **Pull Request**를 생성합니다.
6. 리뷰어를 지정하고, 코멘트를 받으면 수정해서 다시 push 합니다.

## 완료 기준
- [ ] 새 브랜치에서 작업했다 (main 직접 커밋 X)
- [ ] 자기소개 파일을 추가했다
- [ ] 의미 있는 커밋 메시지를 작성했다
- [ ] PR을 열고 링크를 제출했다

> 정답 예시는 `../solution/students/`를 참고하세요.
