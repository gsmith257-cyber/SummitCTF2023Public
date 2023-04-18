FROM ubuntu

#update the repository sources list
ARG DEBIAN_FRONTEND=noninteractive 
RUN apt update

RUN apt-get install -y php
RUN apt-get install -y php-dom
RUN apt-get install -y apache2 && apt-get clean

#ENTRYPOINT ["/usr/sbin/apache2", "-k", "start"]

#ENV APACHE_RUN_USER www-data
#ENV APACHE_RUN_GROUP www-data
#ENV APACHE_LOG_DIR /var/log/apache2

RUN useradd -rm -ms /bin/bash icecreamman

COPY icecreamman.html /var/www/html
COPY icecream.php /var/www/html
COPY index.html /var/www/html
COPY selection.php /var/www/html
COPY assets /var/www/html/assets
COPY resources /var/www/html/resources
COPY flag.txt /home/icecreamman

RUN chown -R icecreamman:icecreamman /var/www/html
RUN chown -R icecreamman:icecreamman /home/icecreamman

RUN chmod -R 755 /var/www/html
#RUN chown -R www-data:www-data /var/www/html


EXPOSE 80
CMD apachectl -D FOREGROUND
