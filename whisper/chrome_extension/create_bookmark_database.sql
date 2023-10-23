-- Check if the 'bookmarks' database exists
SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = 'bookmarks';

-- If 'bookmarks' database does not exist, create it
CREATE DATABASE IF NOT EXISTS bookmarks;

-- Switch to the 'bookmarks' database
USE bookmarks;

-- Create the 'videos' table if it doesn't exist
CREATE TABLE IF NOT EXISTS videos (
    video_id INT NOT NULL AUTO_INCREMENT,
    video_link VARCHAR(255) NOT NULL,
    PRIMARY KEY (video_id)
);

-- Create the 'bookmarks' table with a foreign key reference to 'videos' table if it doesn't exist
CREATE TABLE IF NOT EXISTS bookmarks (
    bookmark_id INT NOT NULL AUTO_INCREMENT,
    video_id INT,
    bookmark_time TIME,
    description TEXT,
    PRIMARY KEY (bookmark_id),
    INDEX (video_id),
    FOREIGN KEY (video_id) REFERENCES videos (video_id)
);
