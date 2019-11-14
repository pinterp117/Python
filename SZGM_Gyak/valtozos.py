lampa = int()
kszam = 0
for i in range(4):
    while lampa != 0 or lampa != 1:
        lampa = int(input("A lámpa állapota (1-felkapcsolt, 0-lekapcsolt): "))
        if lampa == 1:
            kszam = kszam + 1
            break
        elif lampa == 0:
            break
        else:
            print("A lámpa állapota csak 0 vagy 1 lehet.")
if kszam > 2:
    print("A lámpa felkapcsolódik.")
else:
    print("A lámpa nem kapcsolódik fel.")