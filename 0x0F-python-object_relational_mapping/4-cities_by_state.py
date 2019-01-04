#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], host='localhost',
                         port=3306, db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities JOIN states ON cities.state_id = states.id "
                   "ORDER BY cities.id")
    states = cursor.fetchall()
    cursor.close()
    db.close()
    for state in states:
        print("{}".format(state))
