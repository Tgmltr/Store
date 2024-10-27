CREATE DATABASE IF NOT EXISTS mystore;

USE mystore;

CREATE TABLE IF NOT EXISTS category(
cat_id INT NOT NULL PRIMARY KEY, 
cat_name VARCHAR(100) NOT NULL 
);

INSERT INTO category(cat_id,cat_name)
VALUES
(1,'electronics'),
(2,'groceries'),
(3,'dairy')
;

CREATE TABLE IF NOT EXISTS product (
id INT NOT NULL PRIMARY KEY, 
prod_name VARCHAR(100) NOT NULL,
cat_id INT NOT NULL,
qty INT NOT NULL,
PRICE FLOAT,
FOREIGN KEY (cat_id) REFERENCES category(cat_id)
);

