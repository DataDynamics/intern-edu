-- 컨테이너 첫 기동 시 자동 실행되는 초기화 스크립트
CREATE TABLE products (
    id    SERIAL PRIMARY KEY,
    name  TEXT NOT NULL,
    price INT NOT NULL
);

INSERT INTO products (name, price) VALUES
    ('book', 12000),
    ('food', 8000),
    ('toy', 30000);
