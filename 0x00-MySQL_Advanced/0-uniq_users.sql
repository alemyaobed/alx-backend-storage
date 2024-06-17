-- An sql script that creates a users table
CREATE TABLE
	IF NOT EXISTS users (
		id INTEGER AUTO_INCREMENT PRIMARY KEY,
		email VARCHAR(255) NOT NULL UNIQUE,
		name VARCHAR(255)
	);
