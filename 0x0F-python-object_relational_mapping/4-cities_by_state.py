#!/usr/bin/python3
"""
Title: Cities by states
Description: Script that lists all cities from the database hbtn_0e_4_usa
Author: @a_idk scripting
"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cur = db.cursor()
    """cur.execute(
            "SELECT * FROM states WHERE name LIKE %s", (sys.argv[4])
            )
            """
    cur.execute(
            """SELECT cities.id, cities.name, states.name FROM
            cities INNER JOIN states ON states.id=cities.state_id"""
            )

    states = cur.fetchall()
    for state in states:
        print(state)

    # cleaning up
    cur.close()
    db.close()
