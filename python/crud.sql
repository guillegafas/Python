create database usuarios1;
USE usuarios1;
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    pass VARCHAR(500) NOT NULL
);

