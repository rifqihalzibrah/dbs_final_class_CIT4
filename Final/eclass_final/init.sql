DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
DROP TABLE IF EXISTS topics;
CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL
);
DROP TABLE IF EXISTS submissions;
CREATE TABLE submissions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    topic_id INT,
    body TEXT NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_topic FOREIGN KEY (topic_id) REFERENCES topics(id)
);

INSERT INTO users (id, username, name, password) VALUES (0, 'teacher', 'teacher', 'teacher')