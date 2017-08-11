#!/usr/bin/python3
"""
lists all states with a name starting with N
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    query = """SELECT states.id, states.name FROM states WHERE states.name
    LIKE 'N%' ORDER BY states.id ASC"""
    cur.execute(query)
    for states in cur.fetchall():
        print(states)

    cur.close()
    db.close()
