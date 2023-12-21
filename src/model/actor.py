from src.db.connections import MySQLConnector
from src.db.connections import db_name
import logging

logging.getLogger().setLevel(logging.INFO)


class Actor:
	"""
	A sample Actor class

	"""

	table_name = 'Actors'

	def __init__(self, firstname: str, lastname: str, birthday: str):
		self.actor_id = None
		self.firstname = firstname
		self.lastname = lastname
		self.birthday = birthday

	def __repr__(self):
		return f"{db_name}.{Actor.table_name} ({self.firstname}, {self.lastname}, {self.birthday})"

	def insert_actor(self):
		with MySQLConnector() as conn:
			query = f"""INSERT INTO {db_name}.{Actor.table_name} (firstname, lastname, birthday)
					VALUES ("{self.firstname}", "{self.lastname}", "{self.birthday}")"""
			print(query)
			conn.execute_query(query, commit=False)
			actor_id = conn.execute_query('SELECT LAST_INSERT_ID()')[0][0]
			self.actor_id = actor_id
			return actor_id

	@classmethod
	def get_actor_by_id(cls, find_id):
		"""
		Class method returns Actor object in case passed id is present in the DB.
		:param find_id:
		:return: Actor object
		"""
		with MySQLConnector() as conn:
			res = conn.get_by_id(cls.table_name, find_id)
			if not res:
				return None
			actor = Actor(*res[0][1:])
			actor.actor_id = res[0][0]
			return actor

	def delete_actor(self):
		"""
		Method delete Actor object from the DB
		:return: integer
		"""
		try:
			with MySQLConnector() as conn:
				conn.delete_by_id(self.table_name, self.actor_id)
				deleted = Actor.get_actor_by_id(self.actor_id)
				if deleted is not None:
					logging.log(logging.INFO, f'Delete was NOT successful. \n {deleted}')
					raise ValueError(
						f'Unsuccessful delete of {self.actor_id} - {self.firstname} {self.lastname} actor.'
						f'Please resolve an issue.')
		except Exception as e:
			logging.log(logging.INFO, f'Error: {e}')
			raise e
		logging.log(logging.INFO, f'Delete successful.')

	def update_actor_firstname(self, new_firstname: str):
		if not isinstance(new_firstname, str) or len(new_firstname) > 200:
			raise ValueError(
				f"Provided firstname - {new_firstname} is not valid. Please enter valid and accurate firstname.")
		with MySQLConnector() as conn:
			query = f"UPDATE {db_name}.{Actor.table_name} SET firstname='{new_firstname}' WHERE actor_id ={self.actor_id}"
			conn.execute_query(query)
			self.firstname = new_firstname


def main():
	new_actor = Actor('Drue', 'Berrimor', '1966-01-03')
	print(new_actor)
	actor_id = new_actor.insert_actor()
	print(actor_id)
	actor = Actor.get_actor_by_id(actor_id)
	print(actor)
	new_actor.update_actor_firstname('Druella')
	print(new_actor.firstname)
	new_actor.delete_actor()
	actor = Actor.get_actor_by_id(actor_id)
	print(actor)


if __name__ == "__main__":
	main()
