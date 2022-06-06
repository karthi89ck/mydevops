FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install apache2 -y
COPY index.html /var/www/html
EXPOSE 8091
CMD ["apachectl", "-D", "FOREGROUND"]
