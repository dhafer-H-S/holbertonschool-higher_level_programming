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
        WHERE states.name = %s
        ORDER BY cities.id """, (argv[4], )
    )
    rows = thecursor.fetchall()
    if rows == ():
        print("")
    else:
        for i in range(len(rows)):
            if i == len(rows) - 1:
                print(rows[i][1])
            else:
                print("{}, ".format(rows[i][1]), end="")
    thecursor.close()
    db.close()
