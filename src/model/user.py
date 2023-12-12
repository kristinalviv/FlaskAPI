from src.db.connections import MySQLConnector
from src.db.connections import db_name
import logging

logging.getLogger().setLevel(logging.INFO)

# create user, actors, ratings modules with classes
# create moviecharacter - as a methods within created classes