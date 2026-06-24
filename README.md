# 데이터 엔지니어 인턴 교육 프로그램

대학생 인턴사원을 위한 데이터 엔지니어링 실무 교육 과정입니다.
**문서 + 실습 코드**를 함께 제공하며, 대상에 따라 두 개의 트랙으로 나뉩니다.

## 🧭 나는 어느 트랙인가요?

| 트랙 | 대상 | 시작점 | 기간 |
|------|------|--------|------|
| [🟢 대학생 트랙](tracks/undergraduate/) | 컴퓨터공학을 이제 전공하려는 신입, 프로그래밍 경험 거의 없음 | 완전 기초부터 | 약 14~15주 |
| [🔵 졸업생 트랙](tracks/graduate/) | 대학 졸업생, 기초 프로그래밍 경험 보유, 실무 투입 준비 | 실무 파이프라인 지향 | 약 11~13주 |

> 두 트랙 모두 **AI 시대의 현실과 생존 전략**을 가장 먼저 다룬 뒤, Python·SQL 기초 위에서
> 데이터 엔지니어링으로 나아갑니다.

## 📂 저장소 구조

```
intern-edu/
├── docs/            # 커리큘럼 개요, 학습 경로 등 공통 문서
├── setup/           # 공통 실습 환경 세팅 (Python, Git, Docker)
├── tracks/
│   ├── undergraduate/   # 🟢 대학생 트랙
│   └── graduate/        # 🔵 졸업생 트랙
├── datasets/        # 실습용 공유 샘플 데이터
└── resources/       # 슬라이드, 추천도서, 치트시트, 외부 링크
```

각 트랙은 `modules/NN-주제/` 형태의 모듈로 구성되며, 모든 모듈은 동일한 표준 구조
(`examples/`, `exercises/starter|solution/`, `assessment/`)를 따릅니다. 자세한 내용은
[CONTRIBUTING.md](CONTRIBUTING.md)와 [커리큘럼 개요](docs/curriculum-overview.md)를 참고하세요.

## 🚀 시작하기

1. [setup/README.md](setup/README.md)로 실습 환경을 세팅합니다.
2. 자신의 트랙 `README`를 열어 학습 순서를 확인합니다.
3. 모듈을 순서대로(`00 → 01 → ...`) 진행합니다.

## 📑 핵심 문서

- [커리큘럼 전체 개요](docs/curriculum-overview.md)
- [트랙별 학습 경로](docs/learning-path.md)
- [콘텐츠 작성 가이드 (강사용)](CONTRIBUTING.md)
