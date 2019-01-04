#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], host='localhost',
                         port=3306, db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT name FROM cities "
                   "WHERE state_id="
                   "(SELECT id FROM states WHERE name='{}') ".format(argv[4]))
    states = cursor.fetchall()
    cursor.close()
    db.close()
    out = ""
    for state in states:
        out += state[0]
        out += ', '
    print ("{}".format(out[0:-2]))
