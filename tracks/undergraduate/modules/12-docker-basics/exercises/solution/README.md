# 정답 해설 — Postgres compose

## 핵심
- `image: postgres:16` — 공식 이미지 사용
- `environment` — Postgres 이미지는 `POSTGRES_PASSWORD`(필수), `POSTGRES_DB`로 초기 DB 생성
- `ports: "5432:5432"` — 호스트에서 접속 가능하게 노출
- `volumes`:
  - `pgdata:/var/lib/postgresql/data` — **데이터 영속화** (컨테이너 지워도 보존)
  - `./init.sql:/docker-entrypoint-initdb.d/init.sql:ro` — 이 디렉토리의 `.sql`은
    **컨테이너 첫 기동 시 자동 실행** (테이블 자동 생성). `:ro`는 읽기 전용.

## 확인
```bash
docker compose up -d
docker compose exec db psql -U postgres -d shop -c "SELECT * FROM products;"
# id | name | price 가 3행 나오면 성공
docker compose down
```

## 주의
- `init.sql`은 **볼륨이 비어 있는 첫 기동에만** 실행됩니다. 이미 데이터가 있으면 무시됩니다.
  다시 실행하려면 `docker compose down -v`로 볼륨을 비우세요.
