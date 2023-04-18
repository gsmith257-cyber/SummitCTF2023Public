#!/bin/sh

service mysql start
sleep 3
mysql -u root -e 'CREATE DATABASE summitworks;'
mysql -u root -e 'CREATE TABLE summitworks.users(username varchar(40), password varchar(40));'
mysql -u root -e 'CREATE TABLE summitworks.comments(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, comment TEXT);'
mysql -u root -e 'INSERT INTO summitworks.users (username, password) VALUES ("admin", "@]WD-?e$4dNgLN/(7[t#qS~)?eG$gwd");'
mysql -u root -e 'CREATE USER "admin"@"localhost" IDENTIFIED BY "dHXZjEyfac423VZmeyqNnFBrRR64zjKM";'
mysql -u root -e 'GRANT ALL PRIVILEGES ON * . * TO "admin"@"localhost";'
mysql -u root -e 'FLUSH PRIVILEGES;'


./venv/bin/activate && flask run --host 0.0.0.0
./venv/bin/activate && pip3 install selenium && export PATH=$PATH:/src/ && xvfb-run python3 ./client.py
