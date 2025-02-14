-- CREATE DATABASE myowndb;
USE myowndb;

CREATE TABLE users (
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL,
    `password` VARCHAR(50) NOT NULL,
    UNIQUE (`username`)
);

INSERT INTO users (`username`, `password`) VALUES ('admin', 'admin123');