#!/usr/bin/python3
"""
Title: All cities by state
Description: Script that takes in the name of a state as an argument
    and lists all cities of that state, using the database hbtn_0e_4_usa
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
    search = (
            """SELECT cities.name FROM cities INNER JOIN states
            ON states.id=cities.state_id WHERE states.name=%s""",
            (sys.argv[4],)
            )
    cur.execute(search)

    states = cur.fetchall()
    temp = []
    for state in states:
        if state[4] == sys.argv[4]:
            temp.append(state[2])
    print(", ".join(temp))

    # cleaning up
    cur.close()
    db.close()
