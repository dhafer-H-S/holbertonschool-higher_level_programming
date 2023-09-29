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
        """SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY id """

    )
    rows = thecursor.fetchall()
    for row in rows:
        print(row)
    thecursor.close()
    db.close()
