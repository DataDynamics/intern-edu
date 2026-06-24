# 실습 — 환경 점검 스크립트 완성

개발 환경이 제대로 갖춰졌는지 스스로 확인하는 작은 스크립트를 완성합니다.
(Python 기초는 모듈 06에서 배우지만, 여기서는 빈칸 채우기 수준입니다.)

## 할 일 — `env_check.py`의 TODO를 채우세요
1. `python_version()` — 현재 Python 버전을 "3.x.y" 형태 문자열로 반환
   (힌트: `platform.python_version()`)
2. `is_supported(version)` — 버전 문자열을 받아 메이저가 3이고 마이너가 10 이상이면 True
3. `greet(name)` — `"환경 준비 완료, {name}!"` 형태 문자열 반환

## 검증
```bash
python check.py
```
`✅ 모든 테스트 통과!` 가 목표입니다. (가상환경을 활성화한 상태에서 실행해보세요.)
