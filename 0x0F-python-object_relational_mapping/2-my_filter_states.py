#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name ='{}' ORDER BY id".format(arg))
    my_states = c.fetchall()
    for state in my_states:
        if sys.argv[4] == state[1]:
            print(state)
    c.close()
    db.close()
