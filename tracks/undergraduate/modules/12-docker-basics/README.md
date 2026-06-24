# 모듈 12 — Docker 기초

> **포커스**: 컨테이너 개념, 이미지/볼륨, `docker run`·compose, **Postgres 띄우기**
> **예상 기간**: 1주
> **선행 모듈**: 05 Linux, 10~11 SQL

"제 컴퓨터에선 됐는데요?" — 이 문제를 없애는 도구가 **Docker**입니다. 데이터베이스,
파이프라인 실행 환경, 분석 도구를 **컨테이너**라는 격리된 상자에 담아 어디서나 똑같이
실행합니다. 데이터 엔지니어는 DB·Airflow·Kafka 등을 거의 항상 컨테이너로 띄웁니다.
이 모듈에서는 09~10에서 SQLite로 배운 SQL을, 이번엔 **컨테이너로 띄운 진짜 Postgres**에서
실행해봅니다.

> 💡 실습에는 Docker Desktop(또는 Docker Engine)이 필요합니다. (setup/docker 참고)

---

## 🎯 학습 목표
- 컨테이너·이미지·볼륨의 개념과 가상머신과의 차이를 이해한다
- `docker run`, `ps`, `logs`, `exec`, `stop` 등 기본 명령을 사용한다
- `docker-compose.yml`로 Postgres를 한 번에 띄운다
- 컨테이너로 띄운 Postgres에 접속해 SQL을 실행한다
- 볼륨으로 데이터를 영속화(persist)하는 이유를 안다

---

## 📚 핵심 주제

### 1. 왜 Docker인가
- **이미지(image)**: 실행에 필요한 모든 것을 담은 "설치 패키지"(예: `postgres:16`)
- **컨테이너(container)**: 이미지를 실행한 "인스턴스". 격리된 채 돌아감
- **볼륨(volume)**: 컨테이너가 사라져도 **데이터를 보존**하는 저장소
- VM과 달리 OS를 통째로 복제하지 않아 **가볍고 빠름**

### 2. 기본 명령
```bash
docker run hello-world             # 첫 컨테이너 실행 (이미지 자동 다운로드)
docker pull postgres:16            # 이미지만 미리 받기
docker ps                          # 실행 중인 컨테이너 목록
docker ps -a                       # 멈춘 것까지 전체
docker logs <컨테이너>              # 로그 보기
docker exec -it <컨테이너> bash     # 컨테이너 안으로 들어가기
docker stop <컨테이너>              # 정지
docker rm <컨테이너>                # 삭제
docker images                      # 받은 이미지 목록
```

### 3. docker run 으로 Postgres 띄우기
```bash
docker run --name pg \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=shop \
  -p 5432:5432 \
  -d postgres:16
```
- `-e` 환경변수(비밀번호/DB명), `-p 호스트:컨테이너` 포트 연결, `-d` 백그라운드 실행

### 4. docker compose — 선언적으로 ⭐
명령이 길어지면 `docker-compose.yml` 파일에 적어두고 한 줄로 실행합니다.
```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: shop
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data   # 데이터 영속화

volumes:
  pgdata:
```
```bash
docker compose up -d      # 백그라운드로 띄우기
docker compose ps         # 상태 확인
docker compose logs -f    # 로그 따라가기
docker compose down       # 정지 + 컨테이너 제거 (볼륨은 유지)
```

### 5. Postgres에 접속해 SQL 실행
```bash
# 컨테이너 안의 psql로 바로 접속
docker compose exec db psql -U postgres -d shop

# psql 안에서
shop=# CREATE TABLE t (id INT, name TEXT);
shop=# INSERT INTO t VALUES (1, 'hello');
shop=# SELECT * FROM t;
shop=# \q     -- 종료
```
> SQLite에서 배운 SQL이 그대로 동작합니다. 차이는 "어디서 도는가"일 뿐.

### 6. 볼륨과 데이터 영속화
- 볼륨 없이 띄운 컨테이너를 지우면 **데이터도 사라집니다.**
- `volumes:`로 DB 데이터 디렉토리를 볼륨에 연결하면, `down` 후 다시 `up` 해도 데이터가 남습니다.

---

## 🛠 실습 / 산출물
`exercises/`에서:
1. `docker-compose.yml`을 완성해 Postgres를 띄운다
2. `init.sql`로 테이블을 자동 생성·시드한다
3. `docker compose exec`로 접속해 SQL을 실행하고 결과를 확인한다
- 산출물: 동작하는 `docker-compose.yml` + 접속해서 쿼리한 결과 캡처/기록

> 검증: `docker compose config` 로 컴포즈 파일 문법이 올바른지 먼저 확인할 수 있습니다.

---

## ✅ 완료 기준 (체크리스트)
- [ ] 이미지/컨테이너/볼륨의 차이를 설명할 수 있다
- [ ] `docker ps`, `logs`, `exec`, `stop`을 사용할 수 있다
- [ ] `docker compose up -d`로 Postgres를 띄웠다
- [ ] 컨테이너의 psql에 접속해 SQL을 실행했다
- [ ] 볼륨이 데이터 영속화에 왜 필요한지 설명할 수 있다
- [ ] `exercises/`의 `docker-compose.yml`이 `docker compose config`를 통과한다
- [ ] `assessment/quiz.md`를 모두 풀었다

## 📂 폴더 구성
- `examples/` — 동작하는 compose 예시 + 접속 가이드
- `exercises/starter/` — 완성할 compose/init 골격 + 검증 스크립트
- `exercises/solution/` — 정답
- `assessment/` — 퀴즈 + 완료 체크리스트

## 🔗 참고 자료
- [Docker 공식 — Get started](https://docs.docker.com/get-started/)
- [Postgres 이미지 문서](https://hub.docker.com/_/postgres)
- [Play with Docker (브라우저 실습)](https://labs.play-with-docker.com/)
- 졸업생 트랙 모듈 01(환경)·07(오케스트레이션)에서 컨테이너를 본격 활용합니다.
