-- Check if the 'bookmarks' database exists
SELECT SCHEMA_NAME
FROM INFORMATION_SCHEMA.SCHEMATA
WHERE SCHEMA_NAME = 'bookmarks';

-- If 'bookmarks' database does not exist, create it
CREATE DATABASE IF NOT EXISTS bookmarks;

-- Switch to the 'bookmarks' database
USE bookmarks;