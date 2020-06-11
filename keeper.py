# this is the main file.

import pandas as pd
import mysql.connector
import adder

db = mysql.connector.connect(host="localhost", username="root", password="root")
pointer = db.cursor()
pointer.execute("USE keeper")
print("Welcome tou your personal project keeper, Here's a list of options for you:")
#pointer.execute("SHOW TABLES")
while True:
    print('')
    print(">SHOW CURRENT PROJECTS")
    print(">ADD NEW PROJECT")
    print(">EXIT")
#print(">SHOW LATEST WORK")
    optn = input()
    if optn.upper()=='EXIT':
        break
    elif optn.upper()=='SHOW':
        pointer.execute("SELECT * FROM current_projects")
        for i  in pointer:
            print(i)
    elif optn.upper()=="ADD":
        adder.add(pointer, db)


'''
to print after execution:
for i in pointer:
    print(i)
'''

