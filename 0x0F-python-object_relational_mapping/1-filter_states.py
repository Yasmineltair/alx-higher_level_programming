#!/usr/bin/python3
""" script that lists all states with a name
starting with N (upper N) from the
database hbtn_0e_0_usa """
import MySQLdb
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        port=3306,
        database=argv[3]
     )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for row in result:
        if row[1].startswith("N"):
            print(row)
    cursor.close()
    db.close()
