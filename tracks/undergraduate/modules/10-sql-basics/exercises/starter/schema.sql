-- 고객 / 주문 스키마 (PostgreSQL)
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    category    TEXT NOT NULL,
    amount      INTEGER NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

INSERT INTO customers (id, name, city) VALUES
    (1, '김철수', 'Seoul'),
    (2, '이영희', 'Busan'),
    (3, '박민수', 'Seoul'),
    (4, '최지우', 'Incheon');

INSERT INTO orders (id, customer_id, category, amount) VALUES
    (1, 1, 'book',  12000),
    (2, 1, 'food',   8000),
    (3, 2, 'book',  15000),
    (4, 2, 'toy',   30000),
    (5, 3, 'food',   5500),
    (6, 3, 'book',   3000),
    (7, 1, 'toy',   22000),
    (8, 4, 'food',   9000);
