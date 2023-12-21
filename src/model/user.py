from src.db.connections import MySQLConnector
from src.db.connections import db_name
import logging

logging.getLogger().setLevel(logging.INFO)

class User:
	"""
	A sample User class

	"""

	table_name = 'Users'

	def __init__(self, user_name: str, user_login: str, user_pass: str):
		self.user_id = None
		self.user_name = user_name
		self.user_login = user_login
		self.user_pass = user_pass

	def __repr__(self):
		return f"{db_name}.{User.table_name}({self.user_name}, {self.user_login}, {self.user_pass})"

	def insert_user(self) -> int:
		"""
		Method is used per new user creation.
		It takes user object as a parameter and returns newly created id if insert in DB succeeded.
		:return: integer
		"""
		with MySQLConnector() as conn:
			query = f"""INSERT INTO {db_name}.{User.table_name} (user_name, user_login, user_pass)
					VALUES ("{self.user_name}", "{self.user_login}", "{self.user_pass}")"""
			conn.execute_query(query, commit=False)
			user_id = conn.execute_query('SELECT LAST_INSERT_ID()')[0][0]
			self.user_id = user_id
			return user_id

	@classmethod
	def get_user_by_id(cls, find_id):
		"""
		Class method returns User object in case passed id is present in the DB.
		:param find_id:
		:return: User object
		"""
		with MySQLConnector() as conn:
			res = conn.get_by_id(cls.table_name, find_id)
			if not res:
				return None
			user = User(*res[0][1:])
			user.movie_id = res[0][0]
			return user

	def delete_user(self):
		"""
		Method delete User object from the DB
		:return: integer
		"""
		try:
			with MySQLConnector() as conn:
				conn.delete_by_id(self.table_name, self.user_id)
				deleted = User.get_user_by_id(self.user_id)
				if deleted is not None:
					logging.log(logging.INFO, f'Delete was NOT successful. \n {deleted}')
					raise ValueError(
						f'Unsuccessful delete of {self.user_id}-{self.user_name} user. Please resolve an issue.')
		except Exception as e:
			logging.log(logging.INFO, f'Error: {e}')
			raise e
		logging.log(logging.INFO, f'Delete successful.')

	def update_user_login(self, new_login: str):
		if not isinstance(new_login, str) or len(new_login) > 200:
			raise ValueError(f"Provided login - {new_login} is not valid. Please enter valid and accurate login.")
		with MySQLConnector() as conn:
			query = f"UPDATE {db_name}.{User.table_name} SET user_login='{new_login}' WHERE user_id ={self.user_id}"
			conn.execute_query(query)
			self.user_login = new_login

	def update_user_pass(self, new_pass: str):
		if len(new_pass) > 200:
			raise ValueError(f"Provided password - {new_pass} is not valid. Please enter valid and accurate password.")
		with MySQLConnector() as conn:
			query = f"UPDATE {db_name}.{User.table_name} SET user_pass='{new_pass}' WHERE user_id ={self.user_id}"
			conn.execute_query(query)
			self.user_pass = new_pass


def main():
	new_user = User('Harry', 'h123456', '#$@werfgr789')
	print(new_user)
	new_id = new_user.insert_user()
	print(new_id)
	user = User.get_user_by_id(new_id)
	print(user)
	print(new_user.user_login)
	new_user.update_user_login('H09876543')
	print(new_user.user_login)
	new_user.delete_user()
	user = User.get_user_by_id(new_id)
	print(user)


if __name__ == "__main__":
	main()
