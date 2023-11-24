#CRUD for movie - to do create class and methods

#annotation (decorator)
#@dataclass (static methods, e.g. getdata, nonstatc - crud)

import itertools
from src.db.connections import MySQLConnector

class Movie:
	"""
	A sample Movie class
	"""

	# iter_id = itertools.count()

	def __init__(self, id, name, year_date, genre, rate, actor_id):#todo optional all = None
		self.id = id
		self.name = name
		self.year_date = year_date
		self.genre = genre
		self.rate = rate
		self.actor_id = actor_id

	@property
	def title(self):
		return '{} - ({})'.format(self.name, self.year_date)

	@property.setter
	def name(self, id, new_name):
		if isinstance(new_name) == 'str' and len(new_name) < 200:
			with conn:
				c.execute(f"UPDATE Movie SET name = {new_name} WHERE id = {id}")
				self.name = new_name

	@property.setter
	def name(self, new_genre):
		if isinstance(new_genre) == 'str' and len(new_genre) < 200:
			with conn:
				c.execute(f"UPDATE Movie SET genre = {new_genre} WHERE id = {id}")
				self.genre = new_genre

	@property.setter
	def actor_id(self, new_actor_id):
		if isinstance(new_actor_id) == 'int':
			with conn:
				c.execute(f"ALTER Movie SET actor_id = {new_actor_id} WHERE id = {id}")
				self.actor_id = new_actor_id

	def __repr__(self):
		return "Movie(?, ?, ?, ?, ?)".format(self.name, self.year_date, self.genre, self.rate, self.actor_id)


	# def execute(self, query):
	# 	if not self.connect: self.connect()
	# 	with self.connect.cursor() as my_cursor:
	# 		my_cursor.execute(query)
	# 		self.connect.commit()
	# 		results = my_cursor.fetchall()
	# 		for res in results:
	# 			print(res)

	def insert_film(self, name, year_date, genre, rate, actor_id):
		# if not self.connect: self.connect() -- QQQ do I need this? should I import MySQLConnector? or in main?
		# in tot al what proper steps to connect first and then run statements
		with self.connect.cursor() as my_cursor:
			my_cursor.execute(f"")
			results = my_cursor.fetchall()
			for res in results:
				print(res)

	# def delete_film(self, id):



#QQQ - is it ok to have updates within @property and additional standart methods for insert/delete

#todo CRUD all
