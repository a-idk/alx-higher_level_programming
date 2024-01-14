#!/usr/bin/python3
"""
Title: Get all states
Description: script that lists all states from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM states")

    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
