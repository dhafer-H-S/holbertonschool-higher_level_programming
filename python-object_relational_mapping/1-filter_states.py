#!/usr/bin/python3
"""
 a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],

    )
    thecursor = db.cursor()
    thecursor.execute(
        "SELECT id, name FROM states WHERE name LIKE BINARY 'N%'ORDER BY id")
    rows = thecursor.fetchall()
    for row in rows:
        print(row)
    thecursor.close()
    db.close()