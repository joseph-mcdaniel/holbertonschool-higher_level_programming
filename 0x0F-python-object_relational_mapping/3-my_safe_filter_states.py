#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name='{:s}' \
    ORDER BY id ASC".format(argv[4])
    cur.execute(query)
    for states in cur.fetchall():
        print(states)
