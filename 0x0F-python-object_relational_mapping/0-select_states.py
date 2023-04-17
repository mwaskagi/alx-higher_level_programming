#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],passwd=argv[2],db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    fetch = c.fetchall()
    for state in fetch:
        print(state)
    c.close()
    db.close()
