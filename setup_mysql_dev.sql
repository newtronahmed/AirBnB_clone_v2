--CREATE databae if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_dev_db;

--CREATE user if it does not exists
CREATE USER IF NOT EXISTS 'hbtn_dev'@'localhost' IDENTIFIED WITH 'hbnb_dev_pwd';

--GRANT ALL priviledges on the db  to the created user
GRANT ALL ON hbtn_dev_db.* TO 'hbtn_dev'@'localhost';

--GRANT select priviledge to read from perfomance scema
GRANT SELECT ON performance_schema.* TO 'hbtn_dev'@'localhost';
