class Versenyzo:
    def __init__(self, nev, rajtszam, pontok, atlag):
        self.nev = nev
        self.rajtszam = rajtszam
        self.pontok = pontok
        self.atlag = atlag


versenyzokszama = int(input("Hány versenyző vett részt a versenyen: "))
birakszama = int(input("Hány bíra volt a versenyen: "))
versenyzo = []
for i in range(versenyzokszama):
    versenyzo = Versenyzo.nev = input("Versenyző neve: ")


print(versenyzo)