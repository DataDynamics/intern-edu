# 모듈 06 — 퀴즈 정답

1. 작업 디렉토리(수정) → `add` → 스테이징(커밋 후보) → `commit` → 로컬 저장소(이력) → `push` → 원격.
2. `add`는 변경을 **커밋 후보(스테이징)** 로 올리는 것, `commit`은 스테이징된 것을 **이력으로 확정**하는 것.
3. main을 항상 배포 가능한 안정 상태로 유지 / 코드 리뷰를 통한 품질·지식 공유 / 변경 단위를 격리해 충돌·롤백이 쉬움.
4.
   ```bash
   git status
   git add report.py
   git commit -m "Add weekly report"
   git push
   ```
5. `git switch -c feature/login` (구버전: `git checkout -b feature/login`)
6. 첫 줄 50자 내외 명령형 요약 / 무엇을 했는지 명확 / 필요시 "왜"를 본문에 설명 (이 중 2개).
7. 두 브랜치가 **같은 줄을 다르게** 수정한 채 병합될 때 발생. `<<<<<<< ======= >>>>>>>` 구역에서 올바른 내용만 남기고 마커 삭제 → `add` → `commit`.
8. Git이 **추적하지 않을 파일**을 지정. 예: `.venv/`, `.env`, `__pycache__/`, `*.log`.
