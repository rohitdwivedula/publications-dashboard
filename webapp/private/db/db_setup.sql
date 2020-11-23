CREATE DATABASE student_marks;
USE student_marks;

CREATE TABLE users (
	user_email varchar(255) NOT NULL,
	user_key varchar(255) NOT NULL,
	name varchar(255) NOT NULL,
	salt varchar(255) NOT NULL,
	admin bit,
	PRIMARY KEY (user_email)
);

CREATE TABLE eval (
	eval_id int NOT NULL AUTO_INCREMENT,
	eval_name varchar(255) NOT NULL,
	date_of_eval date NOT NULL,
	description varchar(255),
	max_marks int NOT NULL,
	PRIMARY KEY (eval_id)
);

CREATE TABLE marks (
	record_number int NOT NULL AUTO_INCREMENT,
	user_email varchar(255) NOT NULL,
	eval_id int NOT NULL,
	score int NOT NULL,
	verified bit,
	PRIMARY KEY (record_number),
	FOREIGN KEY (user_email) REFERENCES users(user_email),
	FOREIGN KEY (eval_id) REFERENCES eval (eval_id)
);

ALTER TABLE marks ADD UNIQUE(user_email, eval_id);