#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("""SELECT cities.name FROM
                cities LEFT JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (match,))
    rows = cur.fetchall()
    tempo = list(row[0] for row in rows)
    print(*tempo, sep=", ")
    cur.close()
    db.close()
