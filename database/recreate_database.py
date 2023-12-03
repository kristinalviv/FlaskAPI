from src.db.connections import MySQLConnector
import os
from config import mysql_user, mysql_pass, host, port #todo - discuss if it is needed to import config additionally?
#todo - discuss if we need to push log files

#todo - to discuss if classes are needed here?


def establish_conn(*args, login=mysql_user, password=mysql_pass, host=host, port=port, **kwargs):  # todo - to discuss is it ok? or getattr(self, 'login') is better?
	if args:
		login = args[0]
		password = args[1]
	elif kwargs:
		login = kwargs['mysql_user']
		password = kwargs['mysql_pass']
	with MySQLConnector(login, password) as new_conn:
		return new_conn


def recreate_db_and_tables(conn):
	with open('DDL.sql', 'r') as ddl:
		queries = ddl.read().split(';')
		for query in queries:
			conn.execute_query(query)
	print(f'Successfully recreated {os.path.basename(ddl.name)}.')

def reinsert_data(conn):
	with open('initial_data_insert.sql', 'r') as data:
		queries = data.read().split(';')
		for query in queries:
			conn.execute_query(query)
	print(f'Successfully inserteed data from  {os.path.basename(data.name)}.')


def main():
	print('Starting')
	conn = establish_conn()
	print('Connection done')
	recreate_db_and_tables(conn)
	print('DB and tables insert done')
	# reinsert_data(conn)
	# print('Data reinsert done')


# with open('initial_data_insert.sql', 'r') as initial_data_insert:
# 	rerun_statements(initial_data_insert)

if __name__ == "__main__":
	main()


#todo - discuss questions - why this module excutes commands from connections.py main function? (line 47-50)
#todo - discuss questions - if we create conn using context manager how to handle query execution in another
# function. since with conteext manager, after it exits, __exit__ method is called and connections closes.

#
# /usr/local/bin/python3 /Users/khrystyna/Desktop/My/Projects/FlaskAPI/database/recreate_database.py
# Starting
# <src.db.connections.MySQLConnector object at 0x1013f7f40>
# <pymysql.connections.Connection object at 0x10175a3e0>
# True
# connection closed.
# Connection done
# create DATABASE IF NOT EXISTS movies_db
#
# USE movies_db
#
# CREATE TABLE if not exists Movies
# (
# 	movie_id INT AUTO_INCREMENT PRIMARY KEY,
# title VARCHAR(255) NOT NULL,
# 					   year_date YEAR(4) NOT NULL,
# 											 description VARCHAR(255),
# 														 budget_in_millions int NOT NULL
# )
#
#
# CREATE TABLE if not exists Actors
# (
# 	actor_id INT AUTO_INCREMENT PRIMARY KEY,
# firstname VARCHAR(255) NOT NULL,
# 						   lastname VARCHAR(255) NOT NULL,
# 													 birthday date NOT NULL
# )
#
#
# CREATE TABLE if not exists Users
# (
# 	user_id INT AUTO_INCREMENT PRIMARY KEY,
# user_name VARCHAR(255) NOT NULL,
# 						   user_login VARCHAR(255) NOT NULL,
# 													   user_pass VARCHAR(255) NOT NULL
# )
#
#
# CREATE TABLE if not exists Ratings
# (
# 	user_id int NOT NULL,
# movie_id int NOT NULL,
# score int NOT NULL,
# review VARCHAR(1024),
# create_date DATETIME DEFAULT (CURRENT_DATE),
# 					 FOREIGN KEY(movie_id) REFERENCES Movies(movie_id),
# 													  FOREIGN KEY(user_id) REFERENCES Users(user_id),
# 																					  PRIMARY KEY(user_id, movie_id)
# )
#
#
# CREATE TABLE if not exists MovieCharacter
# (
# 	movie_id int NOT NULL,
# actor_id int NOT NULL,
# character_name VARCHAR(255) NOT NULL,
# 								FOREIGN KEY(movie_id) REFERENCES Movies(movie_id),
# 																 FOREIGN KEY(actor_id) REFERENCES Actors(actor_id),
# 																								  PRIMARY KEY(actor_id, movie_id)
# )
#
#
# Successfully recreated DDL.sql.
# DB and tables insert done
# --- Logging error ---
# Traceback (most recent call last):
# File "/Users/khrystyna/Desktop/My/Projects/FlaskAPI/src/db/connections.py", line 55, in execute_query
# c.execute(query)
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/cursors.py", line 158, in execute
# result = self._query(query)
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/cursors.py", line 325, in _query
# conn.query(q)
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/connections.py", line 549, in query
# self._affected_rows = self._read_query_result(unbuffered=unbuffered)
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/connections.py", line 779, in _read_query_result
# result.read()
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/connections.py", line 1157, in read
# first_packet = self.connection._read_packet()
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/connections.py", line 729, in _read_packet
# packet.raise_for_error()
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/protocol.py", line 221, in raise_for_error
# err.raise_mysql_exception(self._data)
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/pymysql/err.py", line 143, in raise_mysql_exception
# raise errorclass(errno, errval)
# pymysql.err.OperationalError: (1065, 'Query was empty')
#
# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/logging/__init__.py", line 1100, in emit
# msg = self.format(record)
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/logging/__init__.py", line 943, in format
# return fmt.format(record)
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/logging/__init__.py", line 678, in format
# record.message = record.getMessage()
# File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/logging/__init__.py", line 368, in getMessage
# msg = msg % self.args
# TypeError: not all arguments converted during string formatting
# Call stack:
# File "/Users/khrystyna/Desktop/My/Projects/FlaskAPI/database/recreate_database.py", line 43, in <module>
# main()
# File "/Users/khrystyna/Desktop/My/Projects/FlaskAPI/database/recreate_database.py", line 35, in main
# recreate_db_and_tables(conn)
# File "/Users/khrystyna/Desktop/My/Projects/FlaskAPI/database/recreate_database.py", line 27, in recreate_db_and_tables
# conn.execute_query(query)
# File "/Users/khrystyna/Desktop/My/Projects/FlaskAPI/src/db/connections.py", line 59, in execute_query
# logging.log(logging.INFO, 'MySQL error: ', e)
# Message: 'MySQL error: '
# Arguments: (OperationalError(1065, 'Query was empty'),)
#
# Process finished with exit code 0

