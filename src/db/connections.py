import pymysql
import logging
from datetime import datetime

from config import mysql_user, mysql_pass, host, port


class MySQLConnector:
	"""
	#add description

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

		else:
			# todo check if connection is still alive else reopen
			pass
		return self

	def close(self):
		if self.connection:
			self.connection.close()
			logging.log(logging.INFO, f'{datetime.now()} - connection closed.')


if __name__ == "__main__":
	print(mysql_user)
	with MySQLConnector(mysql_user, mysql_pass) as new_conn:
		print(new_conn)
		print(new_conn.connection)

