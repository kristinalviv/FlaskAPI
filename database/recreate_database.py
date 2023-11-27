# to run ddl and initial_data_insert

from src.db.connections import MySQLConnector

# with
conn = MySQLConnector()
conn.execute_query()


def rerun_statements(file):
	content = file.read()
	parsed = content.split(';')
	for statement in parsed:  # try:
		conn.execute_query(statement)
	print(f'Successfully recreated {file.__name__}.')


with open('DDL.sql', 'r') as ddl:
	rerun_statements(ddl)

with open('initial_data_insert.sql', 'r') as initial_data_insert:
	rerun_statements(initial_data_insert)
