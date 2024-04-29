
DROP DATABASE ChatPET;
DROP USER 'testuser';

CREATE USER 'testuser' IDENTIFIED BY 'testuser';
CREATE DATABASE ChatPET;
USE chatapp
GRANT ALL PRIVILEGES ON ChatPET.* TO 'testuser';

CREATE TABLE users (
    uid varchar(255) PRIMARY KEY,
    user_name varchar(255) UNIQUE NOT NULL,
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
    message text
);

CREATE TABLES posts(
    post_id serial PRIMARY KEY,
    post text NOT NULL,
    uid VARCHAR(255) REFERENCES users(uid)
);

CREATE TABLES images(
    image_id SERIAL PRIMARY KEY,
    post_id INT NOT NULL,
    image_data BLOB NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(post_id) 
);

INSERT INTO users(uid, user_name, email, password)VALUES('99ace1a1-725b-be03-2455-56a66be4a079','テスト','pet@gmail.com','778c04806dd4ba98b1bbff9083433a8f67aed60a3346dfa16913fb5e875e462d');
INSERT INTO channels(id, uid, name)VALUES(1, '99ace1a1-725b-be03-2455-56a66be4a079','犬');
INSERT INTO messages(id, uid, cid, message)VALUES(1, '99ace1a1-725b-be03-2455-56a66be4a079', '1', '犬です')