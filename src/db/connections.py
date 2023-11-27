import pymysql
import logging
from datetime import datetime

from config import mysql_user, mysql_pass, host, port


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
		# todo check if connection is still alive else reopen --changed a little, implemented in execute
		return self.connection
		#return self.connection.cursor() #then within context manager in 72 line __enter__ executed - QQQ

	def execute_query(self, query):
		try:
			if not self.connection.open:
				logging.log(logging.INFO, 'Connection is closed. Trying to reconnect')
				c = self.connect()
				if not c.connection.open:
					logging.log('Could not connect.')
			logging.log(logging.INFO, 'Connection is open. Executing query')
			with self.connection.cursor() as c:
				c.execute(query)
				c.commit()
				return c.fetchall()
		except pymysql.err.OperationalError as e:
			logging.log(logging.INFO, e)
		except Exception as e:
			logging.log(logging.INFO, e)


	def close(self):
		if self.connection:
			self.connection.close()
			logging.log(logging.INFO, f'{datetime.now()} - connection closed.')


if __name__ == "__main__":
	print(mysql_user)
	# with MySQLConnector(mysql_user, mysql_pass) as new_conn: - QQQ
	new_conn = MySQLConnector(mysql_user, mysql_pass)
	print(new_conn)
	test = new_conn.connect()
	print(test.cursor().connection)
	print(test.cursor().connection.open)
	new_conn.execute_query('SHOW DATABASES;')
	new_conn.close()
	print(new_conn)
	print(test.cursor().connection)
	print(test.cursor().connection.open)

