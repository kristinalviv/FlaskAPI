import pymysql
import logging
from datetime import datetime
import os
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

	def execute_query(self, query):
		try:
			logging.log(logging.INFO, f'Trying to execute following query: {query}')
			if not self.connection or not self.connection.open:
				raise Exception('Connection is not established')
			with self.connection.cursor() as c:
				c.execute(
					query)  # todo - if commit can be added here instead of all other modules; add as parameter here
				res = c.fetchall()
				logging.log(logging.INFO, f'Successfully executed.')
				return res
		except pymysql.err.OperationalError as e:
			logging.log(logging.INFO, f'MySQL error: {e}')
			raise e
		except pymysql.err.ProgrammingError as e:
			logging.log(logging.INFO, f'Data error: {e.args[0]} error id - "{e.args[1]}" error message')
			raise e
		except Exception as e:
			logging.log(logging.INFO, f'Error: {e}')
			raise e

	def get_by_id(self, table: str = None, entity_id: int = None):
		logging.log(logging.INFO, f'Trying to query {entity_id} ID in {table} TABLE.')
		if not entity_id or not table:
			raise Exception(
				'Please define both TABLE and identificator. /n Currently TABLE is {table} and ID is {entity_id}')
		column_name_query = f"SHOW KEYS FROM {table} WHERE KEY_NAME = 'PRIMARY'"
		column_name = self.execute_query(column_name_query)
		query = f"SELECT * FROM {table} where {column_name} = {entity_id}"
		result = self.execute_query(query)
		logging.log(logging.INFO, f'{column_name} with {entity_id} ID in {table} TABLE is {res}')
		return result

	def delete_by_id(self, table: str = None, entity_id: int = None):  # todo - update as get_by_id
		logging.log(logging.INFO, f'Trying to delete {entity_id} ID in {table} TABLE.')
		if entity_id and table:
			column_name_query = f"SHOW KEYS FROM {table} WHERE KEY_NAME = 'PRIMARY'"
			column_name = self.execute_query(column_name_query)
			query = f"DELETE FROM {table} where {column_name} = {entity_id}"
			result = self.execute_query(query)
			logging.log(logging.INFO, f'Successfully deleted {entity_id} {column_name} in {table} TABLE.')
			return result
		else:
			print('Please define both TABLE and identificator. /n Currently TABLE is {table} and ID is {entity_id}')

	def show_all_data(self, table: str =None):  # todo - update as get_by_id
		if table:
			query = f"SELECT * FROM {table}"
			result = self.execute_query(query)
			logging.log(logging.INFO, f'{table} TABLE has following data: {res}')
			return result
		else:
			print(f'Please define TABLE. /n Currently TABLE is {table}.')

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
