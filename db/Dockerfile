FROM mysql:latest 

WORKDIR /docker-entrypoint-initdb.d

COPY ./build_db.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
