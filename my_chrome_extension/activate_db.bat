@echo off

:: Set environment variables (adjust these values)
set MYSQL_USER=root
set MYSQL_BIN_PATH="C:\Program Files\MySQL\MySQL Server 8.0\bin"
set SQL_SCRIPT_PATH="C:\Users\yarden\Desktop\Yarden\Personal\Yardenregev\my_chrome_extension\create_bookmark_database.sql"

:: Add the MySQL bin directory to the PATH temporarily
set PATH=%MYSQL_BIN_PATH%;%PATH%

:: Execute the MySQL command
mysql -u %MYSQL_USER% -p < %SQL_SCRIPT_PATH%

:: Restore the original PATH
set PATH=%PATH%
