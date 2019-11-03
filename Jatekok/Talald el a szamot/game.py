import random
elet = 5
szam = random.randint(1,10)
while elet >= 0:
    tipp = int(input("Tippelj egy számot: "))
    if tipp == szam:
        print("Eltaláltad!")
        break
    else:
        print("Nem találtad el, próbáld újra! A maradék életed:", elet)
        elet = elet - 1
print("")
if elet == -1:
    print("Jaj ne, elvesztetted az összes életed, meghaltál! Játék vége! A keresett szám", szam, "volt.")
else:
    print("Nyertél, vége a játéknak!")