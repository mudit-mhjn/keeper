
def showAll(db, pointer):
    print('')
    pointer.execute("SELECT name FROM current_projects")
    for i in pointer:
        for project_name in i:
            print(project_name)

def showProject(db, pointer):
    pass
