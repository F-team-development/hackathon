
DROP DATABASE ChatPET;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE ChatPET;
USE ChatPET
GRANT ALL PRIVILEGES ON ChatPET.* TO 'testuser';

CREATE TABLE users (
    uid varchar(255) PRIMARY KEY,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    name varchar(255) UNIQUE NOT NULL
);

CREATE TABLE messages (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    cid integer REFERENCES channels(id) ON DELETE CASCADE,
    message text,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE images(
    image_id SERIAL PRIMARY KEY,
    image_data BLOB NOT NULL
);

CREATE TABLE createProfile (
    user_name varchar(255) PRIMARY KEY,
    user_icon varchar(255) DEFAULT 'テスト用猫アイコン.png',
    user_bio varchar(140),
    uid varchar(255) REFERENCES users(uid)
);

INSERT INTO users(uid, email, password)VALUES('99ace1a1-725b-be03-2455-56a66be4a079','pet@gmail.com','778c04806dd4ba98b1bbff9083433a8f67aed60a3346dfa16913fb5e875e462d');
INSERT INTO channels(id, uid, name)VALUES(1, '99ace1a1-725b-be03-2455-56a66be4a079','犬');
INSERT INTO messages(id, uid, cid, message, created_at)VALUES(1, '99ace1a1-725b-be03-2455-56a66be4a079', 1, '犬です','2024-05-17 10:00:00');
INSERT INTO images(image_id,image_data)VALUES(1,LOAD_FILE('/static/img/ロゴアイコン.jpg'));
INSERT INTO createProfile(user_name, user_icon, user_bio, uid)VALUES('テスト', 'テスト用猫アイコン.png', 'よろしくお願いします', '99ace1a1-725b-be03-2455-56a66be4a079');