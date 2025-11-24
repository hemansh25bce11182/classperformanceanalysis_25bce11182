studs = []
def showMenu():
    print("\n  --- MAIN MENU ---")
    print("1.Add student")
    print("2.Show all")
    print("3.Class report")
    print("4.Find student")
    print("5.Exit")
def addStud():
    name1 = input("Name: ")
    mks = input("Marks: ")
    try:
        mks = float(mks)
    except:
        print("numbers only plz")
        return
    att = input("Attendance%: ")
    try:
        att = float(att)
    except:
        att = 0
    intr = input("Internal marks: ")
    try:
        intr = float(intr)
    except:
        intr = 0
    studs.append((name1, mks, att, intr))
    print("ok added.")
def dispAll():
    if len(studs) == 0:
        print("empty list...")
        return
    print("\n-- ALL STUDENTS --")
    for xy in studs:
        print("Name :", xy[0])
        print("Marks:", xy[1])
        print("Att:", xy[2])
        print("Internal:", xy[3])
        print("----------------------")
def classRep():
    if len(studs) == 0:
        print("no data, add first")
        return
    t1 = t2 = t3 = 0
    hi = -999
    lo = 999999
    hiName = ""
    loName = ""
    fails = 0
    for s in studs:
        mk = s[1]
        at = s[2]
        it = s[3]
        t1 += mk
        t2 += at
        t3 += it
        if mk < 10:
            fails = fails + 1
        if mk > hi:
            hi = mk
            hiName = s[0]
        if mk < lo:
            lo = mk
            loName = s[0]
    cnt = len(studs)
    a1 = t1 / cnt
    a2 = t2 / cnt
    a3 = t3 / cnt
    passp = round(((cnt - fails) / cnt) * 100, 2)
    print("\n=== Class Stats ===")
    print("Total:", cnt)
    print("Avg Marks:", a1)
    print("Avg Att:", a2)
    print("Avg Internal:", a3)
    print("Topper:", hiName, hi)
    print("Lowest:", loName, lo)
    print("Fails:", fails)
    print("Pass%:", passp)
    print("===================")
def findStud():
    if len(studs) == 0:
        print("nothing yet")
        return
    nm = input("Enter name: ").strip().lower()
    found = 0
    totm = tota = toti = 0
    for kk in studs:
        totm += kk[1]
        tota += kk[2]
        toti += kk[3]
    ct = len(studs)
    avgM = totm / ct
    avgA = tota / ct
    avgI = toti / ct
    for s in studs:
        if s[0].lower() == nm:
            found = 1
            print("\n---- Student ----")
            print("Name:", s[0])
            print("Marks:", s[1])
            print("Attendance:", s[2])
            print("Internal:", s[3])
            print("\nCompared to class::")
            print("Marks:", "above" if s[1] >= avgM else "below")
            print("Att:", "above" if s[2] >= avgA else "below")
            print("Int:", "above" if s[3] >= avgI else "below")
            if s[1] >= 35:
                print("Result: PASS")
            else:
                print("Result: FAIL")
            break
    if found == 0:
        print("not found.")
while True:
    showMenu()
    c = input("option: ")
    if c == "1":
        addStud()
    elif c == "2":
        dispAll()
    elif c == "3":
        classRep()
    elif c == "4":
        findStud()
    elif c == "5":
        print("bye")
        break
    else:
        print("wrong")
