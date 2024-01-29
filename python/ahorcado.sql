create database ahorcado;
use ahorcado;
CREATE TABLE palabras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    palabra VARCHAR(50) NOT NULL
);
INSERT INTO palabras (palabra) VALUES
    ('hola'),
    ('python'),
    ('programacion'),
    ('juego'),
    ('computadora');
CREATE TABLE intentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    palabra_adivinada VARCHAR(255) NOT NULL
);