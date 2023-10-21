-- Creates a database `hbtn_0d_usa` & a table `states`
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(
       id INT NOT NULL PRIMARY KEY UNIQUE,
       name VARCHAR(256) NOT NULL
);