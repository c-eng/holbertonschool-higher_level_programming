#!/usr/bin/python3
"""Lists all states of hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv
db = MySQLdb.connect(user=argv[1], passwd=argv[2], host='localhost',
                     port=3306, db=argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id")
states = cursor.fetchall()
for state in states:
    print("{}".format(state))
