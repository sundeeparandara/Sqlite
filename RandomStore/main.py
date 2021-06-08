import sqlite3
import random
import time
from datetime import datetime


def create_db(name_of_db):

    connection = sqlite3.connect(name_of_db)
    cursor = connection.cursor()
    # command1 = """CREATE TABLE IF NOT EXISTS
    # random_table(ID INTEGER PRIMARY KEY, random_value REAL)"""
    command1 = """CREATE TABLE IF NOT EXISTS
    random_table(event_time INTEGER, random_value REAL)"""
    cursor.execute(command1)

def update_db(name_of_db, event_time, random_value):
    connection = sqlite3.connect(name_of_db)
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO random_table VALUES ({event_time},{random_value})")
    connection.commit()

rounds = 10
i = 0
name_of_db = 'random.db'



while i < rounds:

    event_time = int(time.time())
    value = random.uniform(0,1)

    if i == 0:
        print("creating db")
        print(event_time)
        # a = datetime.now()
        create_db(name_of_db)
        time.sleep(1)
        # b = datetime.now()
        # c = b - a
        # print(f"{c.seconds} s")

    else:
        print(f"adding entry {i}")
        print(event_time)
        #a = datetime.now()
        update_db(name_of_db, event_time,value)
        time.sleep(1)
        # b = datetime.now()
        # c = b - a
        # print(f"{c.seconds} s")




    i += 1
