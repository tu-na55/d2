set global local_infile = 1;

-- CREATE DATABASE sample;
USE sample;

-- CREATE TABLE users(
create table IF not exists `users`(
    `id` INT(20) AUTO_INCREMENT,
    `name` varchar(80) not null,
    `email` VARCHAR(255),
    PRIMARY KEY (`id`)
);
-- engine=innodb default charset=utf8mb4 collate=utf8mb4_bin;
-- );

--  id (11) PRIMARY KEY AUTO_INCREMENT NOT NULL,
--  `name` VARCHAR(20) NOT NULL,
--  `name` VARCHAR(64) NOT NULL,

    -- `created_at` Datetime DEFAULT NULL,
    -- `updated_at` Datetime DEFAULT NULL,

INSERT INTO users(name,email) VALUES('sample','sample@sample.com');
INSERT INTO users(name,email) VALUES('test','test@test.com');
INSERT INTO users(name,email) VALUES('app','app@app.com');

