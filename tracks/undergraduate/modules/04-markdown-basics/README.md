# 모듈 04 — Markdown 기초

> **포커스**: 문서화, README/PR 작성, GitHub Flavored Markdown(GFM)
> **예상 기간**: 2~3일
> **선행 모듈**: 03 개발 환경 & 터미널

데이터 엔지니어는 **글로 소통**합니다. README로 프로젝트를 설명하고, PR 설명으로 변경
이유를 남기고, 분석 리포트를 작성하고, 문서로 동료에게 지식을 전달합니다. 이 모든 것의
공통 언어가 **Markdown**입니다. 지금 읽고 있는 이 문서도 Markdown으로 작성됐습니다.

> 💡 Markdown은 5분이면 배우지만 평생 씁니다. 다음 모듈 06(Git & 협업)에서 PR 설명을
> 쓸 때, 그리고 모든 실습의 리포트에서 바로 사용합니다.

---

## 🎯 학습 목표
- 제목·강조·목록·링크·이미지를 Markdown으로 작성한다
- 코드 블록과 표(table)를 만든다
- 인용문·체크리스트 등 GitHub 확장 문법(GFM)을 사용한다
- 좋은 README의 구조를 안다
- VSCode/GitHub에서 미리보기로 결과를 확인한다

---

## 📚 핵심 주제

### 1. 제목 (Heading)
`#`의 개수로 단계를 표현합니다 (1~6단계).
```markdown
# 제목 1 (가장 큼)
## 제목 2
### 제목 3
```

### 2. 강조 (Emphasis)
```markdown
**굵게**      → 굵게
*기울임*      → 기울임
~~취소선~~    → 취소선
`인라인 코드`  → 코드
```

### 3. 목록 (List)
```markdown
- 순서 없는 목록 (- 또는 *)
- 두 번째 항목
  - 들여쓰기로 하위 항목

1. 순서 있는 목록
2. 두 번째
```

### 4. 링크 & 이미지
```markdown
[표시할 글자](https://example.com)        ← 링크
![대체 텍스트](path/to/image.png)          ← 이미지 (앞에 ! )
```

### 5. 코드 블록 ⭐
백틱 3개로 감싸고, 언어를 적으면 문법 강조(syntax highlighting)가 됩니다.
````markdown
```python
def hello():
    print("hi")
```
````

### 6. 표 (Table)
```markdown
| 이름 | 역할 |
|------|------|
| 수집 | API에서 데이터 |
| 저장 | DB에 적재 |
```
- 헤더 아래 `|---|` 구분선이 **필수**입니다.

### 7. 인용문 & 구분선
```markdown
> 인용문 (팁, 주의사항에 자주 씀)

---   ← 가로 구분선
```

### 8. GitHub 확장 (GFM) — 체크리스트
```markdown
- [ ] 아직 안 한 일
- [x] 완료한 일
```
> 이 교육의 모든 모듈 `✅ 완료 기준`이 바로 이 체크리스트 문법입니다.

### 9. 좋은 README의 구조
```markdown
# 프로젝트 이름
한 줄 소개

## 설치
## 사용법
## 예시
## 라이선스
```

### 10. 미리보기 (Preview)
- **VSCode**: `.md` 파일에서 `Cmd/Ctrl + Shift + V`
- **GitHub**: 저장소에 올리면 자동으로 렌더링되어 보임

---

## 🛠 실습 / 산출물
`exercises/`에서 요구 문법을 모두 포함한 **자기소개 문서(`profile.md`)** 를 작성합니다.
- 제목/강조/목록/링크/코드블록/표/체크리스트/인용문을 모두 사용
- `python check.py`가 각 요소가 들어있는지 검사
- 산출물: `check.py`를 통과하는 `profile.md`

---

## ✅ 완료 기준 (체크리스트)
- [ ] 제목(#)과 강조(**)를 쓸 수 있다
- [ ] 순서 있는/없는 목록을 만들 수 있다
- [ ] 링크와 코드 블록을 작성할 수 있다
- [ ] 표(table)를 만들 수 있다
- [ ] 체크리스트·인용문 같은 GFM 문법을 쓸 수 있다
- [ ] `exercises/`의 `profile.md`가 `check.py`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 모든 문법을 보여주는 `cheatsheet.md`
- `exercises/starter/` — 작성할 `profile.md` 골격 + 자가 검증
- `exercises/solution/` — 정답 예시
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [GitHub — Markdown 기본 문법](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Markdown Guide (한국어)](https://www.markdownguide.org/)
- 모듈 06(Git & 협업)에서 이 Markdown으로 **PR 설명**을 작성합니다.
