#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in states table where name matches argument
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
            f"SELECT * FROM states WHERE name LIKE '{argv[4]}'\
            ORDER BY states.id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
