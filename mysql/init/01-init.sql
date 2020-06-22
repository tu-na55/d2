CREATE DATABASE IF NOT EXISTS sample CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;

CREATE USER IF NOT EXISTS 'tuser'@'%' IDENTIFIED BY 'tpass';

GRANT ALL PRIVILEGES ON sample.* TO 'tuser'@'%';
-- GRANT ALL ON sample.* TO `tuser`;

FLUSH PRIVILEGES;
