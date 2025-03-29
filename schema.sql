CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE chugs (
    id INTEGER PRIMARY KEY,
    drink TEXT,
    clock TIME,
    amount INTEGER,
    alcohol INTEGER,
    user_id INTEGER REFRENCES users
);