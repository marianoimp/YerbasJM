CREATE DATABASE IF NOT EXISTS Yerbas;

USE Yerbas;

CREATE TABLE categorias(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) UNIQUE,
    descripcion TEXT(200)
);

CREATE TABLE productos (
	id INT AUTO_INCREMENT PRIMARY KEY ,
	nombre VARCHAR(100),
    descripción TEXT(200),
    precio INT,
    stock INT DEFAULT 5,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY ,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(250),
    rol ENUM('admin','usuario') DEFAULT 'usuario'

);

CREATE TABLE carrito (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    producto_id INT,
    cantidad INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);



INSERT INTO categorias(nombre,descripcion) VALUES('TERMOS', 'Termos elegantes y duraderos para mantener tus bebidas a la temperatura ideal');
INSERT INTO usuarios (nombre,email,password) VALUES ('Juan','jp@gmail.com','1234');
