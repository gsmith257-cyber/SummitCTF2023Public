CREATE DATABASE secret;
USE secret;
CREATE TABLE shhhhh (username VARCHAR(50), password VARCHAR(50));
INSERT INTO shhhhh (username, password) VALUES ('caesar', 'etubrute');
INSERT INTO shhhhh (username, password) VALUES ('flag', 'FhzzvgPGS{Zl5DY_15_P001}');

CREATE USER 'user'@'%' IDENTIFIED BY 'user';
GRANT ALL PRIVILEGES ON secret.* TO 'user'@'%';
FLUSH PRIVILEGES;
