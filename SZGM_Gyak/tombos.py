array = []
lampa = int()
for i in range(4):
    while lampa != 0 or lampa != 1:
        lampa = int(input("A lámpa állapota (1-felkapcsolt, 0-lekapcsolt): "))
        if ((lampa == 0) or (lampa == 1)):
            array.append(lampa)
            break
        else:
            print("A lámpa állapota csak 0 vagy 1 lehet.")
if array.count(1) > 2:
    print("A lámpa felkapcsolódik.")
else:
    print("A lámpa nem kapcsolódik fel.")