#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
    )
    cur = db.cursor()
    cur.execute(
            "SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.states_id = states.id \
            ORDER BY states.id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
