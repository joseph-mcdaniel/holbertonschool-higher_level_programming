#!/usr/bin/python3
"""
takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT states.id, states.name FROM states WHERE states.name \
    LIKE BINARY '{}' ORDER BY states.id ASC".format(argv[4])
    cur.execute(query)
    for states in cur.fetchall():
        print(states)
