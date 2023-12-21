from src.db.connections import MySQLConnector
from src.db.connections import db_name
from src.model.movie import Movie
import logging

logging.getLogger().setLevel(logging.INFO)


class Rating:
	"""
	A class, which represents movie rating data

	"""

	table_name = 'Ratings'

	def __init__(self, score, movie_id, user_id, review, create_date):
		self.score = score
		self.movie_id = movie_id
		self.user_id = user_id
		self.review = review
		self.create_date = create_date

	def __repr__(self):
		return f"{db_name}.{Rating.table_name} ({self.score}, {self.movie_id}, {self.user_id}, {self.review}, " \
			   f"{self.create_date})"

	def insert_rating(self) -> int:
		"""
		Method is used per new rating creation.
		It takes rating object as a parameter and returns newly created id if insert in DB succeeded.
		:return: integer
		"""
		with MySQLConnector() as conn:
			exist_query = f"""SELECT * FROM {db_name}.{Rating.table_name} WHERE user_id = {self.user_id} 
			and movie_id = {self.movie_id}"""
			exists = conn.execute_query(exist_query)
			if exists is None:
				query = f"""INSERT INTO {db_name}.{Rating.table_name} (score, movie_id, user_id, review, create_date)
						VALUES ("{self.score}", "{self.movie_id}", "{self.user_id}", "{self.review}", "{self.create_date}")"""
				conn.execute_query(query)
			else:
				logging.log(logging.INFO, f'Rating for {self.movie_id} by {self.user_id} was already submitted.')
				raise Exception(f'Rating for {self.movie_id} by {self.user_id} was already submitted. '
								f'Please use update method if rating should be fixed.')

	@classmethod
	def get_rates_by_movie_id(cls, find_id):
		"""
		Class method returns Rate object in case passed movie id is present in the DB.
		:param find_id:
		:return: User object
		"""
		with MySQLConnector() as conn:
			res = conn.get_by_id(cls.table_name, 'movie_id', find_id)
			if not res:
				return None
			rating = [Rating(*i) for i in res]
			return rating

	@classmethod
	def get_rates_by_user_id(cls, find_id):
		"""
		Class method returns Rate object in case passed user id is present in the DB.
		:param find_id:
		:return: User object
		"""
		with MySQLConnector() as conn:
			res = conn.get_by_id(cls.table_name, 'user_id', find_id)
			if not res:
				return None
			ratings = [Rating(*i) for i in res]
			return ratings

	@staticmethod
	def calculate_rates_statistic_per_movie_id(dataset):
		"""
		Method calculate max, min, avg score rate per collection of rates
		:param dataset:
		:return:
		"""
		print(type(dataset))
		if not type(dataset) == "<class 'list'>":
			dataset = list(dataset)
		max_rate = max(dataset, key=lambda x: x[1])[0]
		print(f'Max score is: {max_rate}')
		min_rate = min(dataset, key=lambda x: x[1])[0]
		print(f'Min score is: {min_rate}')
		avg_rate = round(sum(map(lambda x: x[1], dataset))/len(dataset), 1)
		print(f'Average score is: {avg_rate}')
		# avg_rate_movie = [x[0] for x in dataset if x[1] == avg_rate][0]
		# print(f'Movie with average score is: {avg_rate_movie}')


	@classmethod
	def total_rates_statistic(cls):
		with MySQLConnector() as conn:
			query = f"SELECT movie_id, score FROM {db_name}.{cls.table_name}"
			res = conn.execute_query(query)
			print(res)
			max_rate_movie = max(list(res), key=lambda x: x[1])[0]
			max_movie = Movie.get_movie_by_id(max_rate_movie)
			max_movie_title = max_movie.title
			print(f'Movie with max score is: {max_movie_title}')
			min_rate_movie = min(list(res), key=lambda x: x[1])[0]
			min_movie = Movie.get_movie_by_id(min_rate_movie)
			min_movie_title = min_movie.title
			print(f'Movie with min score is: {min_movie_title}')
			avg_rate = round(sum(map(lambda x: x[1], list(res)))/len(list(res)), 1)
			print(f'Average movie score is: {avg_rate}')
			avg_rate_movie = [x[0] for x in list(res) if x[1] == avg_rate][0]
			avg_movie = Movie.get_movie_by_id(avg_rate_movie)
			avg_movie_title = avg_movie.title
			print(f'Movie with average score is: {avg_movie_title}')

	@classmethod
	def rates_statistic_by_movie(cls):
		with MySQLConnector() as conn:
			query = f"SELECT movie_id, score FROM {db_name}.{cls.table_name}"
			res = conn.execute_query(query)
			data = {k: [y for x,y in list(res) if x == k] for k in {x for x,y in list(res)}}
			for k, values in data.items():
				print(k, values)
				movie = Movie.get_movie_by_id(k)
				movie_title = movie.title
				movie_max_rate = max(map(lambda x: x, values))
				print(f'Movie "{movie_title}" max score is: {movie_max_rate}')
				movie_min_rate = min(map(lambda x: x, values))
				print(f'Movie "{movie_title}" min score is: {movie_min_rate}')
				avg_rate = sum(map(lambda x: x, values))/len(values)
				print(f'Movie "{movie_title}" average score is: {avg_rate}')
				# movie_max_rate = {k: max(map(lambda x: x, v)) for k,v in values}
				# print(f'Movie "{movie}" max score is: {movie_max_rate}')
				# movie_min_rate = {k: min(map(lambda x: x, v)) for k,v in values}
				# print(f'Movie "{movie}" min score is: {movie_min_rate}')
				# avg_rate = {k: sum(map(lambda x: x, v))/len(v) for k,v in values}
				# print(f'Movie "{movie}" average score is: {avg_rate}')
				# avg_rate_movie = [x[0] for x in list(res) if x[1] == avg_rate][0]
				# print(f'Movie average score is: {avg_rate_movie}')


def main():
	# new_rate = Rating(8, 20, 5, 'much liked', '2002-11-29')
	# print(new_rate)
	rate = Rating.get_rates_by_movie_id(30)
	print(rate)
	print(rate[0].user_id, rate[0].score)
	user_rate = Rating.get_rates_by_user_id(19)
	print(user_rate)
	Rating.total_rates_statistic()
	Rating.rates_statistic_by_movie()


if __name__ == "__main__":
	main()
