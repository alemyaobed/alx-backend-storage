-- A script that creates a user table with an enumeration
CREATE TABLE
    IF NOT EXISTS users (
        id INTEGER AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
        country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
    );
