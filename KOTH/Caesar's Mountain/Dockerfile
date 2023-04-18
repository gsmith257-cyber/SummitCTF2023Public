FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
        nmap \
        open-vm-tools \
        openssh-server \
        supervisor \
        sudo 

RUN apt-get update --fix-missing
RUN apt-get install apache2 -y
RUN apt-get install apache2-utils -y
RUN apt-get install mysql-server -y
RUN apt-get install lynx -y
RUN apt-get install php -y
RUN apt-get install phpmyadmin -y
RUN apt-get install vim -y

RUN useradd -ms /bin/bash caesar
RUN useradd -ms /bin/bash mountaineer

EXPOSE 22
EXPOSE 80
EXPOSE 8081
EXPOSE 3306

RUN echo 'root:highestoncaesarsmountain' | chpasswd
RUN echo 'caesar:stabbedintheback' | chpasswd
RUN echo 'mountaineer:password123' | chpasswd


RUN echo "[program:sshd]\ncommand=/usr/sbin/sshd -D\nautorestart=true" > /etc/supervisor/conf.d/sshd.conf
RUN echo "[program:scorechecker]\ncommand=/bin/agent-check -file /root/king.txt -apikey summitCTF2023\nautorestart=true" > /etc/supervisor/conf.d/scorechecker.conf
RUN echo "[program:apache2]\ncommand=/usr/sbin/apache2ctl -k start" > /etc/supervisor/conf.d/apache2.conf
RUN echo "[program:mysql]\ncommand=/usr/sbin/service mysql start" > /etc/supervisor/conf.d/mysql.conf


COPY website1 /var/www/html
RUN chmod 777 /var/www/html
#RUN mkdir /var/www/html/uploads
RUN chmod 777 /var/www/html/uploads
RUN mkdir /var/www/html2
RUN chmod 777 /var/www/html2
COPY website2 /var/www/html2
COPY website2admin /var/www/html2/admin
COPY websiteconfigs/001-default.conf /etc/apache2/sites-enabled/001-default.conf
RUN chmod 777 /etc/apache2/sites-enabled/001-default.conf
#COPY websiteconfigs /etc/apache2/sites-enabled
COPY websiteconfigs/001-default.conf /etc/apache2/sites-available/001-default.conf
RUN chmod 777 /etc/apache2/sites-available/001-default.conf
#COPY websiteconfigs /etc/apache2/sites-available
RUN rm /etc/apache2/ports.conf
COPY ports.conf /etc/apache2/ports.conf
RUN chmod 777 /etc/apache2/ports.conf
RUN echo "ServerName 127.0.0.1" >> /etc/apache2/apache2.conf
RUN echo "AddType application/x-httpd-php .html .htm" >> /etc/apache2/mods-enabled/mime.conf

RUN touch /var/www/html/flag.txt
RUN touch /var/www/html2/admin/flag.txt
RUN touch /tmp/flag.txt
RUN touch /home/mountaineer/flag.txt
RUN touch /home/caesar/user.txt
RUN touch /root/root.txt
RUN touch /root/king.txt
RUN echo 'FhzzvgPGS{1_y0i3_gu3_z0hag41a5}' > /var/www/html/flag.txt
RUN echo 'FhzzvgPGS{o4px_fg4oo3q_4t41a}' > /var/www/html2/admin/flag.txt
RUN echo 'FhzzvgPGS{u1tu3fg_0a_p4rf4ef_z0hag41a}' > /tmp/flag.txt
RUN echo 'FhzzvgPGS{1_j1yy_a3i3e_s0et3g_gu1f}' > /home/mountaineer/flag.txt
RUN echo 'FhzzvgPGS{p4rf4ef_y0fg_u1f_u0z3}' > /home/caesar/user.txt
RUN echo 'FhzzvgPGS{gu3_z0hag41a_1f_z1a3}' > /root/root.txt
COPY script.py /tmp/script.py
RUN chmod 777 /tmp/script.py

# Set up MySQL

RUN service mysql start && \
    mysqladmin -u root password 'highestoncaesarsmountain'
    
COPY secret.sql /tmp/secret.sql
RUN service mysql start && \
    mysql -u root  --password='highestoncaesarsmountain' < /tmp/secret.sql
RUN rm /tmp/secret.sql
RUN rm /etc/mysql/mysql.conf.d/mysqld.cnf
COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf

RUN service mysql start

#setup scorechecker
COPY scoreChecker/dist/agent.linux /bin/agent-check
RUN chmod +x /bin/agent-check

# Give all users sudo permission for vi
RUN echo 'ALL ALL=(ALL) NOPASSWD: /usr/bin/vi' >> /etc/sudoers
RUN echo 'ALL ALL=(ALL) NOPASSWD: /tmp/script.py' >> /etc/sudoers
RUN echo 'www-data ALL=(ALL) NOPASSWD: /tmp/script.py' >> /etc/sudoers

RUN mkdir /run/sshd

#CMD ["/usr/sbin/apache2ctl -k start"]
CMD ["supervisord", "-n"]
#CMD ["/usr/sbin/apache2ctl start"]
