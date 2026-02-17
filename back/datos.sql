CREATE DATABASE IF NOT EXISTS Yerbas;

USE Yerbas;

CREATE TABLE productos (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nombre VARCHAR(100),
    precio INT,
    stock INT DEFAULT 5
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY ,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(250)

);

CREATE TABLE carrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    producto_id INT,
    cantidad INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);

INSERT INTO productos(nombre,precio) VALUES('TERMOS', 5000);
INSERT INTO usuarios (nombre,email,password) VALUES ('Juan','jp@gmail.com','1234');
