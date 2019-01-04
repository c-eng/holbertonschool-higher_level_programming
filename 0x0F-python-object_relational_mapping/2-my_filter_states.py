#!/usr/bin/python3
"""Lists all states of hbtn_0e_0_usa which match passed argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], host='localhost',
                         port=3306, db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()
    cursor.close()
    db.close()
    for state in states:
        if state[1] == argv[4]:
            print("{}".format(state))
