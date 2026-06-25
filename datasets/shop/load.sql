-- shop 샘플을 현재 접속한 PostgreSQL DB에 적재합니다.
-- 사용법(이 폴더 안에서):  psql -d <DB이름> -f load.sql
-- \copy 는 클라이언트(psql)에서 파일을 읽으므로 서버 권한이 필요 없습니다.
\i schema.sql
\copy customers   FROM 'customers.csv'   WITH (FORMAT csv, HEADER true)
\copy products    FROM 'products.csv'    WITH (FORMAT csv, HEADER true)
\copy orders      FROM 'orders.csv'      WITH (FORMAT csv, HEADER true)
\copy order_items FROM 'order_items.csv' WITH (FORMAT csv, HEADER true)
