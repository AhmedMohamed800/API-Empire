CREATE DATABASE IF NOT EXISTS api_db;

USE api_db;
CREATE TABLE IF NOT EXISTS auth (
    id INT PRIMARY KEY AUTO_INCREMENT,
    hashed_key VARCHAR(255),
    max_req INT,
    used_req INT
);

CREATE TABLE IF NOT EXISTS user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE,
    hashed_password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    session_id VARCHAR(255),
    reset_token VARCHAR(255),
    role ENUM('admin', 'user') DEFAULT 'user',
    auth_id INT,
    FOREIGN KEY (auth_id) REFERENCES auth(id)
);

CREATE TABLE IF NOT EXISTS requests (
    id INT PRIMARY KEY AUTO_INCREMENT,
    method ENUM('GET', 'POST', 'PUT', 'DELETE'),
    status_code INT,
    path VARCHAR(255),
    date VARCHAR(255),
    HTTP_version VARCHAR(255),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE IF NOT EXISTS API (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    description TEXT,
    category VARCHAR(255),
    image_cover TEXT
);

CREATE TABLE IF NOT EXISTS endpoint (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    url VARCHAR(255),
    description TEXT,
    method ENUM('GET', 'POST', 'PUT', 'DELETE'),
    response_ex TEXT,
    api_id INT,
    category VARCHAR(255),
    FOREIGN KEY (api_id) REFERENCES API(id)
);

CREATE TABLE IF NOT EXISTS headers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description TEXT,
    type ENUM('string', 'int','float', 'boolean', 'array', 'object'),
    endpoint_id INT,
    FOREIGN KEY (endpoint_id) REFERENCES endpoint(id)
);

CREATE USER 'api_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON api_db.* TO 'api_user'@'localhost';
FLUSH PRIVILEGES;
