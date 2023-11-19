#!/usr/bin/python3

"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    query = "select cities.id, cities.name ,\
            states.name from cities inner join \
            states on states.id= cities.state_id;"

    cur = db.cursor(query)
    cur.execute()

    rows = cur.fetchall()
    for i in rows:
        print(i)
    # Clean up process
    cur.close()
    db.close()
