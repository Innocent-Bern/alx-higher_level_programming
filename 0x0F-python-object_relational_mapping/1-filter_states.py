#!/usr/bin/python3
"""
script that lists all states with a name starting with N
from the database hbtn_0e_0_usa
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
    cur = db.cursor("""SELECT * FROM states WHERE name
                    LIKE BINARY 'N%' ORDER BY states.id ASC""")
    for row in cur.fetchall():
        print(row)
    cur.execute()
    cur.close()
    db.close()