def add(pointer, db):
    query = "INSERT INTO current_projects(name, details) VALUES(%s, %s)"
    n = input(">PROJECT NAME ")
    o = input(">Enter details?(Y/N): ")
    if o.upper()=="N":
        pass
    else:
        d = input("> ")
    vals = (n, d)
    try:
        pointer.execute(query, vals)
        db.commit()
    except:
        pointer.rollback()
    print("PROJECT CREATED")











