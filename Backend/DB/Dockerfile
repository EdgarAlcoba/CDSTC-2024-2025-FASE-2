FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=${DB_PASSWD}
ENV MYSQL_DATABASE=${DB_NAME}

COPY ./backup.sql /docker-entrypoint-initdb.d/backup.sql

EXPOSE 3306
