CREATE TABLE Organisation (
	org_id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(25),
	domain varchar(50)
); 

CREATE TABLE Researcher (
	researcher_id int AUTO_INCREMENT,
	org_id int,
	name varchar(255),
	h5_index int, 
	h5_index_ten int,
	i10_index int,
	i10_index_ten int,
	citations int,
	PRIMARY KEY (researcher_id),
	FOREIGN KEY (org_id) REFERENCES Organisation(org_id)
);

CREATE TABLE Interests (
	interest_id int AUTO_INCREMENT,
	researcher_id int,
	interest varchar(100),
	PRIMARY KEY (interest_id),
	FOREIGN KEY (researcher_id) REFERENCES Researcher(researcher_id)
);

CREATE TABLE Publication (
	publication_id int AUTO_INCREMENT,
	title varchar(255), 
	year int,
	publisher varchar(50),
	citations int,
	PRIMARY KEY (publication_id)
);

CREATE TABLE Authors (
	authorship_id int AUTO_INCREMENT,
	publication_id int NOT NULL,
	author_id int NOT NULL,
	PRIMARY KEY (authorship_id),
	FOREIGN KEY (publication_id) REFERENCES Publication (publication_id),
	FOREIGN KEY (author_id) REFERENCES Researcher (researcher_id)
);

CREATE TABLE Citations (
	citation_id int AUTO_INCREMENT,
	publication_id int,
	year int,
	citation_count int,
	PRIMARY KEY (citation_id),
	FOREIGN KEY (publication_id) REFERENCES Publication(publication_id)
);
