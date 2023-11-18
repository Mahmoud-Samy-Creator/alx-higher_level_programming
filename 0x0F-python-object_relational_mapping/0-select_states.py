#!/usr/bin/python3

"""
a script that lists all states from
the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

user = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
host = "localhost"
port = 3306

if __name__ == "__main__":
    db = MySQLdb.connect(host=host,
                         user=user,
                         passwd=password,
                         db=database_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDERED BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
