#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT name FROM cities WHERE state_id = (SELECT id FROM states \
    WHERE name = '{}') ORDER BY cities.id ASC".format(argv[4])
    cur.execute(query)
    print(", ".join([row[0] for row in cur.fetchall()]))
