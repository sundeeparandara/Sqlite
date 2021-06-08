import sqlite3
import random


def create_db(name_of_db):

    connection = sqlite3.connect(name_of_db)
    cursor = connection.cursor()
    command1 = """CREATE TABLE IF NOT EXISTS
    random_table(random_value REAL)"""
    cursor.execute(command1)

def update_db(name_of_db, data):
    connection = sqlite3.connect(name_of_db)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO random_table VALUES ({data})")
    connection.commit()


rounds = 100
i = 0
name_of_db = 'random.db'

while i < rounds:

    value = random.uniform(0,1)

    if i == 0:
        create_db(name_of_db)
    else:
        update_db(name_of_db,value)

    i += 1
