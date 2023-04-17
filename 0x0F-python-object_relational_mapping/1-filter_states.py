#!/usr/bin/python3
import MySQLdb
import sys
if __name__ == "__main__":

    db = MySQLdb.connect(user='root',passwd='root', db='hbtn_0e_0_usa')
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    my_states = c.fetchall()
    for state in my_states:
        if state[1][0] == 'N':
            print(state)
