CREATE TABLE products (
    id    SERIAL PRIMARY KEY,
    name  TEXT NOT NULL,
    price INT NOT NULL
);

INSERT INTO products (name, price) VALUES
    ('book', 12000),
    ('food', 8000),
    ('toy', 30000);
