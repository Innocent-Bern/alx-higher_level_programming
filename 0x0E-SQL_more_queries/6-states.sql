-- script that creates the database hbtn_0d_usa
-- and the table states (in the database hbtn_0d_usa

CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS htbn_0d_usa.states (id INT UNIQUE NOT NULL 
	PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);

