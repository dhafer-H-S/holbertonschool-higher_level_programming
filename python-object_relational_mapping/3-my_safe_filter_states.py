#!/usr/bin/python3
"""
 script that takes in an argument and displays all values in
 the states table of hbtn_0e_0_usa where name matches
the argument.
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
        "SELECT * FROM states WHERE name= %s ORDER BY id", (argv[4], ))
    rows = thecursor.fetchall()
    for row in rows:
        print(row)
    thecursor.close()
    db.close()
