--CREATE databae if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_test_db;

--CREATE user if it does not exists
CREATE USER IF NOT EXISTS 'hbtn_user'@'localhost' IDENTIFIED WITH 'hbnb_test_pwd';

--GRANT ALL priviledges on the db  to the created user
GRANT ALL ON hbtn_test_db.* TO 'hbtn_user'@'localhost';

--GRANT select priviledge to read from perfomance scema
GRANT SELECT ON performance_schema.* TO 'hbtn_test'@'localhost';
