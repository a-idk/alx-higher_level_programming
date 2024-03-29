#!/usr/bin/python3
"""
Title: Filter states
Description: script that lists all states with a name starting with
    N (upper N) from the database hbtn_0e_0_usa
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
    cur.execute("SELECT * FROM `states` ORDER BY `id`")

    states = cur.fetchall()
    for state in states:
        if state[1][0] == "N":
            print(state)
    cur.close()
    db.close()
