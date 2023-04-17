#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
    states ON cities.state_id=states.id")
    my_states = c.fetchall()
    i = 0
    for state in my_states:
        if state[2] == sys.argv[4]:
            if i != 0:
                print(", ", end="")
            print("{}".format(state[1]), end="")
            i += 1
    print()
    c.close()
    db.close()
