from src.db.connections import MySQLConnector
import os


def recreate_db_and_tables():
	with MySQLConnector() as conn:
		with open('database/DDL.sql', 'r') as ddl:
			queries = ddl.read().split(';\n')
			for query in queries:
				conn.execute_query(query)
				conn.connection.commit()
		print(f'Successfully recreated {os.path.basename(ddl.name)}.')

def reinsert_data():
	with MySQLConnector() as conn:
		with open('database/initial_data_insert.sql', 'r') as data:
			queries = data.read().split(';\n')
			for query in queries:
				conn.execute_query(query)
				conn.connection.commit()
			print(f'Successfully inserted data from  {os.path.basename(data.name)}.')


def main():
	print('Starting')
	recreate_db_and_tables()
	print('DB and tables insert done')
	reinsert_data()
	print('Data was inserted')


if __name__ == "__main__":
	main()
