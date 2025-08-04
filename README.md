# mydevops
This repository contains basic Dockerfile for creating http ubuntu container.
Yes updated .
once docker-compose up started , it will show error ehen you curl localhost you need to create a table named users
below are the steps

docker exec -it mydevops_db_1 psql -U user -d usersdb

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    dob DATE,
    occupation VARCHAR(100)
);

