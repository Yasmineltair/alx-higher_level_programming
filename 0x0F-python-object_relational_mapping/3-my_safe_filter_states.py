#!/usr/bin/python3
""" script that takes in arguments and displays all values
in the states table """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) == 5:
        db = MySQLdb.connect(
         host="localhost",
         user=argv[1],
         passwd=argv[2],
         database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                  WHERE name LIKE BINARY '{}' \
                  ORDER BY states.id".format(argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
