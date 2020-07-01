# this is the main file.

import pandas as pd
import mysql.connector
import adder
import show

db = mysql.connector.connect(host="localhost", username="root", password="root")
pointer = db.cursor()
pointer.execute("USE keeper")
print('')
print('''###########################################################################
       Welcome to your personal project keeper, Here's a list of options for you
       ###########################################################################

       >SHOW CURRENT PROJECTS
       >ADD NEW PROJECT
       >GOTO PROJECT
       >EXIT''')

#pointer.execute("SHOW TABLES")
while True:
    #print(">SHOW LATEST WORK")
    optn = input()
    if optn.upper()=='EXIT':
        break
    elif optn.upper()=='GOTO':
        show.showProject(db, pointer)

    elif optn.upper()=='SHOW':
        # # TODO: add this in show.showAll()
        show.showAll(db, pointer)
        """
        pointer.execute("SELECT name FROM current_projects")
        for i in pointer:
            for project_name in i:
                print(project_name)
        """
    elif optn.upper()=="ADD":
        adder.addProject(db, pointer)
    else:
        print('INVALID CHOICE- TRY AGAIN')



'''
to print after execution:
for i in pointer:
    print(i)
'''
