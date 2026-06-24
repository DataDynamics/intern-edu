# 실습 — Postgres를 compose로 띄우고 초기화

`docker-compose.yml`을 완성해 Postgres를 띄우고, `init.sql`로 테이블을 자동 생성합니다.

## 할 일
1. `docker-compose.yml`의 `# TODO`를 채웁니다.
   - 이미지: `postgres:16`
   - 환경변수: `POSTGRES_PASSWORD=secret`, `POSTGRES_DB=shop`
   - 포트: 호스트 5432 → 컨테이너 5432
   - 볼륨: 이름 있는 볼륨 `pgdata`를 `/var/lib/postgresql/data`에 연결
   - `init.sql`을 `/docker-entrypoint-initdb.d/`에 마운트 (첫 기동 시 자동 실행)
2. 문법 검증: `bash check.sh` (또는 `docker compose config`)
3. (Docker 설치 시) 실제로 띄워 접속해봅니다.
   ```bash
   docker compose up -d
   docker compose exec db psql -U postgres -d shop -c "SELECT * FROM products;"
   docker compose down
   ```

## init.sql (이미 작성되어 있음)
`products` 테이블을 만들고 샘플 3행을 넣습니다. 컨테이너 첫 기동 시 자동 실행됩니다.
