def backwardChaining(g, r, f, db):
    tempLst = []
    for i in g:
        if i in db:
            tempLst.append(db[i])
            continue

        if i in f:
            tempLst.append(1)
            continue

        for j in r:
            if j[-1] == i:
                if all(backwardChaining(p, r, f, db) for p in j[:-1]):
                    db[i] = 1
                    tempLst.append(1)
                    break
        else:
            db[i] = 0
            tempLst.append(0)
    return tempLst

goal,facts,rules,db =["M"],["A", "B", "C", "D"],[
        [("P"),"Q"],
        [("D","M"),"P"],
        [("B","L"),"M"],
        [("A","B"),"L"],
        [("A","D"),"G"],
        [("G","B"),"C"]],{}

finalResult = backwardChaining(goal, rules, facts, db)
print("Database = ",list(db.keys()))

for goalss in goal: 
  for result in finalResult:
    print(goalss,'is','Found in KB' if result else 'not Found in KB')