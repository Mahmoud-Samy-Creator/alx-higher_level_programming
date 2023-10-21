-- Creates at database cities and table inside database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities
(
       id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
       state_id INT NOT NULL FORIGN KEY(id) REFERENCES states(id),
       name VARCHAR(256) NOT NULL
);
