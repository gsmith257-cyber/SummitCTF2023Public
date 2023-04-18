CREATE DATABASE climbers;
USE climbers;
CREATE TABLE users (
  id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(30) NOT NULL,
  password VARCHAR(30) NOT NULL
);
INSERT INTO users (username, password) VALUES
  ('npurja', '1mountain1love');
INSERT INTO users (username, password) VALUES
  ('Nessie', 'Nessie');

CREATE DATABASE drupal;
USE drupal;
CREATE USER drupal@localhost IDENTIFIED BY "password";
GRANT ALL PRIVILEGES ON drupal.* TO drupal@localhost;
FLUSH PRIVILEGES;
