from src.db.connections import MySQLConnector
from src.db.connections import db_name
import logging

logging.getLogger().setLevel(logging.INFO)


# todo - @dataclass
class Movie:
	"""
	A sample Movie class
	"""

	table_name = 'Movies'

	def __init__(self, title=None, year_date=None, description=None, budget_in_millions=None):
		self.title = title
		# self._title = title
		self.year_date = year_date
		self.description = description
		self.budget_in_millions = budget_in_millions
		self.movie_id = None

	def __repr__(self):
		return f"{db_name}.{Movie.table_name}({self.title}, {self.year_date}, " \
			   f"{self.description}, {self.budget_in_millions}) "

	# @property
	# def title(self):
	# 	return self._title
	#
	# @title.setter
	# def title(self, new_title: str):
	# 	if not isinstance(new_title, str) or len(new_title) > 200:
	# 		raise ValueError(f"Provided name - {new_title} is not valid. Please enter valid and accurate film name.")
	# 	with MySQLConnector() as conn:
	# 		query = f"UPDATE {db_name}.{Movie.table_name} SET title='{new_title}' WHERE movie_id ={self.movie_id}"
	# 		print(query)
	# 		conn.execute_query(query)
	# 		self._title = new_title

	# todo - insert_film should return id - DONE
	# todo - insert_film should insert value form self instead of parameters - DONE

	def insert_film(self) -> int:
		"""
		Method is used per new movie creation.
		It takes movie object as a parameter and returns newly created id if insert in DB succeeded.
		:return: integer
		"""
		with MySQLConnector() as conn:
			query = f"""INSERT INTO {db_name}.{Movie.table_name} (title, year_date, description, budget_in_millions)
					VALUES ("{self.title}", {self.year_date}, "{self.description}", {self.budget_in_millions})"""
			conn.execute_query(query, commit=False)
			movie_id = conn.execute_query('SELECT LAST_INSERT_ID()')[0][0]
			self.movie_id = movie_id
			# conn.connection.commit()
			return movie_id

	@classmethod
	def get_movie_by_id(cls, find_id):
		"""
		Class method returns Movie object in case passed id is present in the DB.
		:param find_id:
		:return:
		"""
		with MySQLConnector() as conn:
			res = conn.get_by_id(cls.table_name, find_id)
			return res

	def delete_film(self):
		"""
		Method delete Movie object from the DB
		:return: integer
		"""
		try:
			with MySQLConnector() as conn:
				conn.delete_by_id(self.table_name, self.movie_id)
				deleted = Movie.get_movie_by_id(self.movie_id)
		except Exception as e:
			logging.log(logging.INFO, f'Error: {e}')
			raise e
		if len(deleted) != 0:
			logging.log(logging.INFO, f'Delete was NOT successful. \n {deleted}')
			raise ValueError(f'Unsuccessful delete of {self.movie_id}-{self.title} movie. Please resolve an issue.')
		else:
			logging.log(logging.INFO, f'Delete successful.')
			print('here')
			del self  # todo - discuss additional del in main is needed

	def update_movie_title(self, new_title: str):
		if not isinstance(new_title, str) or len(new_title) > 200:
			raise ValueError(f"Provided name - {new_title} is not valid. Please enter valid and accurate film name.")
		with MySQLConnector() as conn:
			query = f"UPDATE {db_name}.{Movie.table_name} SET title='{new_title}' WHERE movie_id ={self.movie_id}"
			conn.execute_query(query)
			self.title = new_title

	def update_movie_year(self, new_year: int):
		if not isinstance(new_year, int) or len(new_year) != 4:
			raise ValueError(f"Provided year - {new_year} is not valid. Please enter valid and accurate film year.")
		with MySQLConnector() as conn:
			query = f"UPDATE {db_name}.{Movie.table_name} SET year_date='{new_year}' WHERE movie_id ={self.movie_id}"
			conn.execute_query(query)
			self.year_date = new_year

	def update_movie_description(self, new_description: str):
		if not isinstance(new_description, str) or len(new_description) > 200:
			raise ValueError(f'Provided description - {new_description} is not valid. Please enter valid and accurate'
				'film description.')
		with MySQLConnector() as conn:
			query = f"UPDATE {db_name}.{Movie.table_name} SET description='{new_description}' WHERE movie_id ={self.movie_id}"
			conn.execute_query(query)
			self.description = new_description

	def update_movie_budget_in_millions(self, new_budget: int):
		if not isinstance(new_budget, int) or new_budget < 0:
			raise ValueError(f"Provided budget - {new_budget} is not valid. Please enter valid and accurate film budget.")
		with MySQLConnector() as conn:
			query = f"UPDATE {db_name}.{Movie.table_name} SET budget_in_millions='{new_budget}' WHERE movie_id ={self.movie_id}"
			conn.execute_query(query)
			self.budget_in_millions = new_budget

def main():
	new_movie = Movie("Forrest Gump", 1994, "Drama", 330.2)
	print(new_movie)
	new_id = new_movie.insert_film()
	print(new_id)
	movie = Movie.get_movie_by_id(new_id)
	print(movie)
	print(new_movie.title)
	# new_movie.title += ' 2 version'
	new_movie.update_movie_title(new_movie.title + ' 2')
	print(new_movie.title)
	new_movie.delete_film()
	del new_movie


if __name__ == "__main__":
	main()
