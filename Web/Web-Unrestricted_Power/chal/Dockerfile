FROM richarvey/nginx-php-fpm:latest
RUN mkdir -p /run/nginx
RUN apk add --no-cache nginx-mod-http-lua
RUN apk add --no-cache supervisor
#RUN echo "[program:nginx]\ncommand=\nautostart=true" > /etc/supervisor/conf.d/nginx.conf
#start nginx with supervisor
RUN echo "\n[program:nginx]\ncommand=/usr/sbin/nginx -g 'daemon off;'\nautostart=true" >> /etc/supervisord.conf
ENV PHP_UPLOAD_MAX_FILESIZE 10000
ENV PHP_POST_MAX_SIZE 10000
ENV PHP_MEM_LIMIT 10000
ENV RUN_SCRIPTS 1
RUN touch /var/log/nginx/error.log
RUN mkdir -p /var/www/html/uploads /var/www/html/conf/nginx/ /var/www/html/scripts /data
COPY nginx.conf /var/www/html/conf/nginx/
COPY ./site /var/www/html/
COPY ./flag.txt /
#allow anyone to read the flag.txt file
RUN chmod 444 /flag.txt
COPY upload_dir.sh /var/www/html/scripts/
RUN rm /etc/nginx/sites-available/default.conf
COPY ./default.conf /etc/nginx/sites-available/default.conf

RUN chown -R nginx:nginx /var/www/
RUN chown -R nginx:nginx /var/log/nginx
RUN chmod -R 755 /var/www/

RUN rm /var/www/errors/404.html
COPY ./404.html /var/www/errors/404.html
EXPOSE 80
CMD ["supervisord", "-n"]