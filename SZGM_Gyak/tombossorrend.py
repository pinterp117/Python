def megold():
    tomb = []
    kapcsolo = 0
    for i in range(3):
        while kapcsolo != 0 or kapcsolo != 1:
            kapcsolo = int(input("A kapcsoló állapota (1-fel, 0-le): "))
            feles = int(input("A kapcsoló állapota (1-fel, 0-le): "))
            if (kapcsolo == 0) or (kapcsolo == 1):
                tomb.append(kapcsolo)
                break
            else:
                print("A kapcsoló állapota csak 1 vagy 0 lehet.")
    if tomb.count(1) > 2:
        print("A lámpa felkapcsolódik.")
    else:
        print("A lámpa nem kapcsolódik fel.")


def keres(lehetoseg):
    global lehet
    if lehetoseg == lehet[0]:
        megold()
    elif lehetoseg == lehet[1]:
        megold()
    elif lehetoseg == lehet[2]:
        megold()
    elif lehetoseg == lehet[3]:
        megold()
    elif lehetoseg == lehet[4]:
        megold()
    elif lehetoseg == lehet[5]:
        megold()
    elif lehetoseg == lehet[6]:
        megold()
    elif lehetoseg == lehet[7]:
        megold()
    elif lehetoseg == lehet[8]:
        megold()
    elif lehetoseg == lehet[9]:
        megold()
    elif lehetoseg == lehet[10]:
        megold()
    elif lehetoseg == lehet[11]:
        megold()
    elif lehetoseg == lehet[12]:
        megold()
    elif lehetoseg == lehet[13]:
        megold()
    elif lehetoseg == lehet[14]:
        megold()
    elif lehetoseg == lehet[15]:
        megold()
    elif lehetoseg == lehet[16]:
        megold()
    elif lehetoseg == lehet[17]:
        megold()
    elif lehetoseg == lehet[18]:
        megold()
    elif lehetoseg == lehet[19]:
        megold()
    elif lehetoseg == lehet[20]:
        megold()
    elif lehetoseg == lehet[21]:
        megold()
    elif lehetoseg == lehet[22]:
        megold()
    elif lehetoseg == lehet[23]:
        megold()
    elif lehetoseg == lehet[24]:
        megold()


lehet = ["abcd", "abdc", "acbd", "acdb", "adbc", "adcb", "bacd", "badc", "bcad", "bcda", "bdac", "bdca", "cabd", "cadb", "cbad", "cbda", "cdab", "cdba", "dabc", "dacb", "dbac", "dbca", "dcab", "dcba",]
kerdes = input("Szeretnéd megadni a kapcsolás sorrendjét? (igen/nem) ")
if kerdes == "igen":
    sorrend = input("Mi legyen a sorrend? (A sorrendet kisbetűkkel és szóközök, vesszők nélkül adja meg) ")
    if sorrend in lehet:
        keres(sorrend) == lehet
    else:
        print("Nincs ilyen lehetőség, vagy nem megfelelő a formátum.")


elif kerdes == "nem":
    tomb = []
    kapcsolo = 0
    for i in range(4):
        while kapcsolo != 0 or kapcsolo != 1:
            kapcsolo = int(input("A kapcsoló állapota (1-fel, 0-le): "))
            if (kapcsolo == 0) or (kapcsolo == 1):
                tomb.append(kapcsolo)
                break
            else:
                print("A kapcsoló állapota csak 1 vagy 0 lehet.")
    if tomb.count(1) > 2:
        print("A lámpa felkapcsolódik.")
    else:
        print("A lámpa nem kapcsolódik fel.")
else:
    print("Nincs ilyen válasz.")


