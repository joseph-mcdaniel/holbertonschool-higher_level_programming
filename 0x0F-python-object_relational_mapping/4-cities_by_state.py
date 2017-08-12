#!/usr/bin/python3
"""
lists all cities from databse
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
    LEFT JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id ASC"
    cur.execute(query)
    for states in cur.fetchall():
        print(states)
