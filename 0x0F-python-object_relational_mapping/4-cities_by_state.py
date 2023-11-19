#!/usr/bin/python3

"""
a script that lists all cities
from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(user=user,
                         passwd=password,
                         db=database_name,
                         host=host,
                         port=port)

    query = """SELECT cities.id, cities.name AS city_name,
                states.name AS state_name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id;"""

    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
