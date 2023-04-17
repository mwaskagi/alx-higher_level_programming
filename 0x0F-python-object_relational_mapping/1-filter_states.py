#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],passwd=argv[2],db=argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    my_states = c.fetchall()
    for state in my_states:
        if state[1].startswith("N"):
            print(state)
    c.close()
    db.close()
