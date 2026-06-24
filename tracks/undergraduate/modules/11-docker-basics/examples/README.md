# 예제 — Postgres 컨테이너 실행

## 1. 띄우기
```bash
docker compose up -d
docker compose ps          # 상태 확인 (health: running)
```

## 2. 접속해서 SQL 실행
```bash
docker compose exec db psql -U postgres -d shop
```
```sql
CREATE TABLE t (id INT, name TEXT);
INSERT INTO t VALUES (1, 'hello'), (2, 'docker');
SELECT * FROM t;
\q
```

## 3. 정리
```bash
docker compose down        # 컨테이너 제거 (볼륨 pgdata는 유지 → 데이터 보존)
docker compose down -v     # 볼륨까지 삭제 (데이터 완전 삭제)
```

## 문법만 검증 (데몬 없이)
```bash
docker compose config      # YAML/설정이 올바른지 파싱만 수행
```
