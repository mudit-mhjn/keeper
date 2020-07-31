def addProject(db, pointer):
    query = "INSERT INTO current_projects(name, details) VALUES(%s, %s)"
    n = input(">PROJECT NAME ")
    o = input(">Enter details?(Y/N): ")
    if o.upper()=="N":
        vals = (n, None)
        pass
    else:
        d = input("> ")
        vals = (n, d)
    try:
        pointer.execute(query, vals)
        db.commit()
    except:
        pointer.rollback()

    sql = '''CREATE TABLE {}(
        TODOS VARCHAR(50),
        ADDED DATE
    )'''.format(n)
    #print(sql)
    pointer.execute(sql)
    print("PROJECT CREATED")


"""
# TODO: TO add reminder in the selected
"""
