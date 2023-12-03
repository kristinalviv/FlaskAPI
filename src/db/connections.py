import pymysql
import logging
from datetime import datetime

from config import mysql_user, mysql_pass, host, port

logging.basicConfig(filename='logging.log',
					filemode='a')
logging.getLogger().setLevel(logging.INFO)


class MySQLConnector:
	"""

	Please use this class per establishing MySQL connection.
	login, password, host and port are defined by default, hence may be omitted
	This class instances have following methods:
	connect - to establish connection and returns a cursor;
	execute - to execute query, which should be passed as a first parameter as well as connection.
	In case connection is not open, reopening will be performed;
	close - to close established connection.

	"""

	def __init__(self, login=mysql_user, password=mysql_pass, host=host, port=port):
		self.host = host
		self.port = port
		self.login = login
		self.password = password
		self.connection = None

	def __enter__(self):
		return self.connect()

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()

	def connect(self):
		if not self.connection:
			self.connection = pymysql.connect(host=self.host,
											  port=self.port,
											  user=self.login,
											  passwd=self.password,
											  connect_timeout=5)
			logging.log(logging.INFO, f'{datetime.now()} - opened connection.')
		return self

	def execute_query(self, query): #todo get by id, get all, delete by id,
		try:
			if not self.connection or not self.connection.open:
				logging.log(logging.INFO, 'Connection is closed. Trying to reconnect')
				self.connect()
			logging.log(logging.INFO, 'Connection is open. Executing query')
			with self.connection.cursor() as c:
				c.execute(query)
				res = c.fetchall()
				return res
		except pymysql.err.OperationalError as e:
			logging.log(logging.INFO, 'MySQL error: ', e)
		except pymysql.err.ProgrammingError as e:
			logging.log(logging.INFO, f'Data error: {e.args[0]} error id - "{e.args[1]}" error message')
		except Exception as e:
			logging.log(logging.INFO, 'Error:', e)

	def close(self):
		if self.connection:
			self.connection.close()
			self.connection = None
			logging.log(logging.INFO, f'{datetime.now()} - connection closed.')
			print('connection closed.')


if __name__ == "__main__":
	with MySQLConnector(mysql_user, mysql_pass) as new_conn:
		print(new_conn)
		print(new_conn.connection)
		print(new_conn.connection.open)
		res = new_conn.execute_query('select * from movies_db.MovieCharacter limit 10;')
		print(res)


# INFO:root:2023-12-03 13:46:10.441129 - opened connection.
# INFO:root:Connection is open. Executing query
# INFO:root:Data error: 1146 error id - "Table 'movies_db.moviecharacter' doesn't exist" error message
# INFO:root:2023-12-03 13:46:10.442908 - connection closed.