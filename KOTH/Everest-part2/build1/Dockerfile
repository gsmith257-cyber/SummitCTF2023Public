FROM ubuntu:latest
#update
ENV DEBIAN_FRONTEND=noninteractive
ENV ServerName=everest.summit

RUN sed -i "s/archive.ubuntu./mirrors.aliyun./g" /etc/apt/sources.list
RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list
RUN sed -i "s/security.debian.org/mirrors.ustc.edu.cn/g" /etc/apt/sources.list

RUN apt-get -y update && apt install -y sudo && apt install -y software-properties-common && apt install -y python2 && \ 
    apt install -y python-is-python3 && apt install -y python3 && apt install -y net-tools && \
    apt install -y vim && apt install -y supervisor && apt install -y samba && apt install -y mysql-server && \
    apt install -y phpmyadmin && apt install -y apache2 && apt install -y php && apt install -y php-mysql && apt-get install -y default-jdk maven && \
    apt install -y openssh-server && apt install -y gcc && apt install -y gdb && apt-get install -y  perl libnet-ssleay-perl openssl libauthen-pam-perl libpam-runtime libio-pty-perl	&&\ 
	apt-get  purge  -y  apt-show-versions && rm -rf /var/lib/apt/lists/*


COPY .flg /root/
COPY flag.txt /var/log/
ENV FLAG="SummitCTF{Alw4ys_st4y_ch3ck1ng_7he_env1ronm3nt_v4r14bl3s!}"

#copy id-rsa.pub to /srv/ftp/
COPY ./id_rsa /srv/ftp/npurja-backup-key
RUN chmod -R 555 /srv/ftp/
RUN echo "[program:apache2]\ncommand=/usr/sbin/apache2ctl -DFOREGROUND" > /etc/supervisor/conf.d/apache2.conf
#add tomcat
RUN echo "[program:tomcat9]\ncommand=/opt/tomcat/bin/catalina.sh run\nautostart=true" > /etc/supervisor/conf.d/tomcat9.conf
RUN echo "[program:wannaHint]\ncommand=/usr/bin/python3 /root/.test/wannaHint.py\nautostart=true" > /etc/supervisor/conf.d/wannaHint.conf
RUN echo "[program:easyWayIn]\ncommand=/usr/bin/python3 /usr/bin/easyWayIn.py\nautostart=true" > /etc/supervisor/conf.d/easyWayIn.conf
RUN echo "[program:smbd]\ncommand=smbd -F --no-process-group -s /etc/samba/smb.conf\nautorestart=true" > /etc/supervisor/conf.d/smbd.conf
RUN echo "[program:sshd]\ncommand=/usr/sbin/sshd -D\nautorestart=true" > /etc/supervisor/conf.d/sshd.conf
RUN echo "[program:scorechecker]\ncommand=/bin/agent-check -file /root/king.txt -apikey summitCTF2023\nautorestart=true" > /etc/supervisor/conf.d/scorechecker.conf


#create a SetUID binary that runs /bin/bash
RUN echo "#include <stdio.h>\n#include <stdlib.h>\n#include <unistd.h>\nint main() {\nsetuid(0);\nsetgid(0);\nsystem(\"/bin/bash\");\nreturn 0;\n}" > /tmp/suid.c
RUN gcc /tmp/suid.c -o /tmp/suidney
RUN chmod +s /tmp/suidney
RUN rm /tmp/suid.c
#create path injection vuln
RUN echo "#include<unistd.h>\nvoid main()\n{ setuid(0);\nsetgid(0);\nsystem(\"ps\");\n}" > /var/ps.c
RUN gcc /var/ps.c -o /var/ps
RUN chmod +s /var/ps
RUN rm /var/ps.c
#add a cron job that runs every minute as root
RUN echo "* * * * * root /var/ps" > /etc/crontab


ENV usrname=npurja
ENV usrpass=1mTh33K1ng
#setup an smb share that contains the files from /tmp/share. Make anonymous access possible
RUN mkdir /tmp/share
RUN chmod 777 /tmp/share
#move letterToHome.txt to /tmp/share
COPY letterToHome.txt /tmp/share
RUN chmod 777 /tmp/share/letterToHome.txt
RUN echo "[share]" >> /etc/samba/smb.conf
RUN echo "path = /tmp/share" >> /etc/samba/smb.conf
RUN echo "guest ok = yes" >> /etc/samba/smb.conf
RUN echo "read only = yes" >> /etc/samba/smb.conf
RUN echo "browseable = yes" >> /etc/samba/smb.conf
RUN echo "force user = nobody" >> /etc/samba/smb.conf
RUN echo "force group = nogroup" >> /etc/samba/smb.conf
RUN echo "create mask = 0777" >> /etc/samba/smb.conf
RUN echo "directory mask = 0777" >> /etc/samba/smb.conf
RUN echo "public = yes" >> /etc/samba/smb.conf
RUN echo "writable = yes" >> /etc/samba/smb.conf
#add phpmyadmin to apache
RUN ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin
#add phpinfo to apache
RUN echo "<?php phpinfo(); ?>" > /var/www/html/info.php
#move contents of site1 folder to /var/www/html
COPY site1 /var/www/html
#ensure config.php is not internet accessible
RUN chmod 644 /var/www/html/config.php
#create uploads directory
RUN mkdir /var/www/html/uploads
RUN chmod 777 /var/www/html/uploads
#set root password
RUN echo "root:1amTh3KingButBetterer" | chpasswd
#add user npurja
RUN useradd -ms /bin/bash npurja
#set password for npurja
RUN echo "npurja:1mTh33K1ng" | chpasswd
#copy user.txt to /home/npurja and make it owned by npurja
COPY user.txt /home/npurja
RUN chown npurja:nogroup /home/npurja/user.txt
RUN chmod 400 /home/npurja/user.txt

# add users
RUN useradd -ms /bin/bash explorer1
RUN useradd -ms /bin/bash Yeti
RUN useradd -ms /bin/bash Bigfoot
RUN useradd -ms /bin/bash Nessie

# set passwords
RUN echo "explorer1:explore" | chpasswd
RUN echo "Yeti:letmein" | chpasswd
RUN echo "Bigfoot:password" | chpasswd
RUN echo "Nessie:Nessie" | chpasswd

#give Nessie root permissions
RUN echo "Nessie ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

#setup sshd_config
RUN mkdir /run/sshd
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
#setup ssh keys, add id-rsa.pub to authorized_keys
RUN mkdir /home/npurja/.ssh
RUN chmod 700 /home/npurja/.ssh
COPY id_rsa.pub /home/npurja/.ssh/authorized_keys
COPY id_rsa /home/npurja/.ssh/id_rsa
RUN chmod 600 /home/npurja/.ssh/authorized_keys
RUN chown -R npurja:nogroup /home/npurja/.ssh
#add gdb to sudo nopasswd for npurja
RUN echo "npurja ALL=(ALL) NOPASSWD: /usr/bin/gdb" >> /etc/sudoers

RUN chmod -R 755 /var/www/html
RUN chown -R www-data:www-data /var/www/html

#setup tomcat
COPY apache-tomcat-9.0.56.tar.gz /tmp/
RUN mkdir /opt/tomcat
RUN tar xzvf /tmp/apache-tomcat-9.0.56.tar.gz -C /opt/tomcat --strip-components=1
RUN rm /tmp/apache-tomcat-9.0.56.tar.gz
RUN chmod -R 755 /opt/tomcat
RUN chown -R root:root /opt/tomcat
RUN ln -s /opt/tomcat/bin/startup.sh /usr/local/bin/tomcatup
RUN ln -s /opt/tomcat/bin/shutdown.sh /usr/local/bin/tomcatdown
RUN ln -s /opt/tomcat/bin/catalina.sh /usr/local/bin/tomcat

#setup spring
ADD src/ /demo/src
ADD pom.xml /demo
WORKDIR /demo/
RUN mvn clean package
RUN mv target/demo.war /opt/tomcat/webapps/
WORKDIR /

#setup mysql server
# Set the root password for MySQL
RUN service mysql start && \
    mysqladmin -u root password '1mTh33K1ng'

# Create the climbers database and tables
COPY climbers.sql /tmp/climbers.sql
RUN service mysql start && \
    mysql -u root  --password='1mTh33K1ng' < /tmp/climbers.sql
RUN rm /tmp/climbers.sql

COPY easyWayIn.py /usr/bin/easyWayIn.py
RUN chmod +x /usr/bin/easyWayIn.py


COPY root.txt /root/
COPY king.txt /root/

#setup scorechecker
COPY scoreChecker/dist/agent.linux /bin/agent-check
RUN chmod +x /bin/agent-check

#setup ftp server
RUN useradd -m ftpuser
RUN chown -R ftpuser:ftpuser /srv/ftp
#a binary that opens connection on port 6789 and asks if the user is npurja, if yes, it gives the content of /srv/ftp/npurja-backup-key
RUN mkdir /root/.test
COPY wannaHint.py /root/.test/wannaHint.py

RUN echo "export flag=\"SummitCTF{Alw4ys_st4y_ch3ck1ng_7he_env1ronm3nt_v4r14bl3s!}\"" >> /etc/bash.bashrc

#expose port 31337
EXPOSE 31337
#expose port 80
EXPOSE 80
EXPOSE 8080
#expose samba
EXPOSE 445
EXPOSE 139
#expose ssh
EXPOSE 22
#expose wannaHint
EXPOSE 56789
#expose mysql
EXPOSE 3306
#expose easyWayIn
EXPOSE 11111

#start all
CMD ["supervisord", "-n"]