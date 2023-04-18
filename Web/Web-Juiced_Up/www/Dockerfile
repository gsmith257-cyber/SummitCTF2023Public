FROM php:7.0-apache
RUN docker-php-ext-install mysqli
ADD src/ /var/www/html/
RUN chown -R www-data:www-data /var/www/html
RUN chmod 755 /var/www/html/
RUN chmod 644 /var/www/html/.htaccess
