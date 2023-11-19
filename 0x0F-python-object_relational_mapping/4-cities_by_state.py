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
                         host=host,
                         port=port,
                         db=database_name,
                         passwd=password)

    query = """SELECT c.id, c.name, s.name
            FROM states s, cities c
            WHERE c.state_id = s.id
            ORDER BY c.id ASC"""

    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
