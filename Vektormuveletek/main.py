valaszt = ""
dimenzio = ""
a = []
b = []
while((dimenzio != 2) or (dimenzio != 3)):
    dimenzio = int(input("Hány dimenziósak a vektorok: "))
    if dimenzio == 2:
        print("Választott dimenzió:", dimenzio)
        break
    elif dimenzio == 3:
        print("Választott dimenzió:", dimenzio)
        break
    else:
        print("A program nem tudja ezeket a dimenziójú vektorokat kezelni, próbálja újra!")
for i in range(dimenzio):
        a.append(float(input("Kérem az a vektor koordinátáit: ")))
print("")
for i in range(dimenzio):
        b.append(float(input("Kérem a b vektor koordinátáit: ")))
print("")
print("a", a)
print("b", b)
print("Melyik műveletet szeretné elvégezni?\n"
      "1 - összeadás\n"
      "2 - kivonás\n"
      "3 - szorzás lambdával\n"
      "4 - skaláris szorzat\n"
      "0 - kilépés")
while(valaszt != 0):
    if dimenzio == 2:
        valaszt = int(input("A művelet száma: "))
        if valaszt == 1:
            osszeg = [a[0] + b[0], a[1] + b[1]]
            print("a+b", osszeg)
        elif valaszt == 2:
            kulonbseg = [a[0] - b[0], a[1] - b[1]]
            print("a-b", kulonbseg)
        elif valaszt == 3:
            n = input("Melyik vektort szeretné megszorozni: ")
            while ((n != 'a') or (n != b)):
                if n == 'a':
                    lam = int(input("Melyik számmal szeretné megszorozni az a vektort: "))
                    szorzas = [lam * a[0], lam * a[1]]
                    print(lam, "* a", szorzas)
                    break
                elif n == 'b':
                    lam = int(input("Melyik számmal szeretné megszorozni a b vektort: "))
                    szorzas = [lam * b[0], lam * b[1]]
                    print(lam, "* b", szorzas)
                    break
                else:
                    n = input("Nincs ilyen vektor, próbálja újra:  ")
        elif valaszt == 4:
            skalar = ((a[0] * b[0]) + (a[1] * b[1]))
            print("<a,b> = ", round(skalar))
        elif valaszt == 0:
            print("Kilépés a programból!")
            break
        else:
            valaszt = int(input("Ilyen menüpont nem volt, próbálja újra: "))
    elif dimenzio == 3:
        valaszt = int(input("A művelet száma: "))
        if valaszt == 1:
            osszeg = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
            print("a+b", osszeg)
        elif valaszt == 2:
            kulonbseg = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
            print("a-b", kulonbseg)
        elif valaszt == 3:
            n = input("Melyik vektort szeretné megszorozni: ")
            while((n != 'a') or (n != b)):
                if n == 'a':
                    lam = int(input("Melyik számmal szeretné megszorozni az a vektort: "))
                    szorzas = [lam * a[0], lam * a[1], lam * a[2]]
                    print(lam, "* a", szorzas)
                    break
                elif n == 'b':
                    lam = int(input("Melyik számmal szeretné megszorozni a b vektort: "))
                    szorzas = [lam * b[0], lam * b[1], lam * b[2]]
                    print(lam, "* b", szorzas)
                    break
                else:
                    n = input("Nincs ilyen vektor, próbálja újra:  ")
        elif valaszt == 4:
            skalar = (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])
            print("<a,b> = ", round(skalar))
        elif valaszt == 0:
            print("Kilépés a programból!")
            break
        else:
            valaszt = int(input("Ilyen menüpont nem volt, próbálja újra: "))