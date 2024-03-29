#!/usr/bin/python3
"""  script that takes in an argument and
displays all values in the states table of
hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
      host="localhost",
      user=argv[1],
      passwd=argv[2],
      database=argv[3]
     )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                  WHERE name LIKE BINARY '{}' \
                  ORDER BY states.id".format(argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
