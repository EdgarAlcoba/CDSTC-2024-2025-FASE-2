FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
ENV MYSQL_DATABASE=${MYSQL_DATABASE}

COPY ./backup.sql /docker-entrypoint-initdb.d/backup.sql

EXPOSE 3306
