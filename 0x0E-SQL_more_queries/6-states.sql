-- Creates hbtn_0d_usa database and states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL
);
