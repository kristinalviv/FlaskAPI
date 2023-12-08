from src.db.connections import MySQLConnector
from config import mysql_user, mysql_pass, host, port

#todo - @dataclass
class Movie:
	"""
	A sample Movie class
	"""

	table_name = 'Movies'

	def __init__(self, title=None, year_date=None, description=None, budget_in_millions=None):
		self.title = title
		self.year_date = year_date
		self.description = description
		self.budget_in_millions = budget_in_millions
	#
	# @property
	# def title(self):
	# 	return '{} - ({})'.format(self.name, self.year_date)
	#
	# @title.setter
	# def name(self, id, new_name):
	# 	if isinstance(new_name) == 'str' and len(new_name) < 200:
	# 		query = f"UPDATE Movies SET name = {new_name} WHERE id = {id}"
	# 		establish_conn(mysql_user, mysql_pass).execute_query(query)
	# 		self.name = new_name #todo - is it needed?
	#
	# @title.setter
	# def description(self, new_description):
	# 	if isinstance(new_description) == 'str' and len(new_description) < 200:
	# 		query = f"UPDATE Movies SET description = {new_description} WHERE id = {id}"
	# 		establish_conn(mysql_user, mysql_pass).execute_query(query)
	# 		self.description = new_description
	#
	# @title.setter
	# def budget_id(self, new_budget):
	# 	if isinstance(new_budget) == 'float' | isinstance(new_budget) == 'int':
	# 		query = f"ALTER Movies SET budget_in_millions = {new_budget} WHERE id = {id}"
	# 		establish_conn(mysql_user, mysql_pass).execute(query)
	# 		self.budget_in_millions = new_budget

	def __repr__(self):
		return f"{Movie.table_name}(?, ?, ?, ?, ?)".format(self.title, self.year_date, self.description, self.budget_in_millions)

	#todo - insert_film should return id

	#todo - insert_film should insert value form self instead of parameters
	# def insert_film(self) -> str:    - use self.name

	def insert_film(self, name: str, year_date: int, description: str, budget: float) -> str:
		with MySQLConnector as conn:
			query = f"""INSERT INTO {Movie.table_name} (title, year_date, description, budget_in_millions)
					VALUES ("{name}", {year_date}, "{description}", {budget})"""
			result = conn.execute_query(query) #todo if execute returns id and return it
			conn.connection.commit() # todo - self id assign
			return result

	def delete_film(self, movie_id: int):
		with MySQLConnector as conn:
			result = conn.delete_by_id(Movie.table_name, movie_id)
			conn.connection.commit()
			return result

	# @staticmethod
	# def get_by_id

	# def update

	# create user, actors, ratings modules with classes
	# create moviecharacter - as a methods within created classes




