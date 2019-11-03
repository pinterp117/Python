tablazat = [
    [8, 0, 1, 0, 2, 6, 0, 4, 0],
    [0, 0, 9, 8, 0, 0, 0, 2, 6],
    [0, 5, 0, 0, 7, 3, 8, 9, 1],
    [1, 3, 2, 0, 8, 0, 0, 7, 9],
    [0, 0, 0, 0, 0, 4, 0, 0, 0],
    [7, 6, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 0, 9, 1, 0],
    [9, 0, 0, 3, 4, 0, 0, 0, 7],
    [0, 8, 3, 0, 9, 0, 0, 5, 4]
]

def megold(tabla):
    print(tabla)
    talal = keres_nulla(tabla)
    if not talal:
        return True
    else:
        sor, oszlop = talal
    for i in range(1, 10):
        if ervenyes(tabla, i, (sor, oszlop)):
            tabla[sor][oszlop] = i
            if megold(tabla):
                return True
            tabla[sor][oszlop] = 0
    return False


def ervenyes(tabla, szam, poz):
    # sor
    for i in range(len(tabla[0])):
        if tabla[poz[0]][i] == szam and poz[1] != i:
            return False
    # oszlop
    for i in range(len(tabla[0])):
        if tabla[i][poz[1]] == szam and poz[0] != i:
            return False
    # cella
    cella_x = poz[1] // 3
    cella_y = poz[0] // 3
    for i in range(cella_y * 3, cella_y * 3 + 3):
        for j in range(cella_x * 3, cella_x * 3 + 3):
            if tabla[i][j] == szam and (i, j) != poz:
                return False
    return True


def print_tabla(tabla):
    for i in range(len(tabla)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(tabla[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            if j == 8:
                print(tabla[i][j])
            else:
                print(str(tabla[i][j]) + " ", end = "")


def keres_nulla(tabla):
    for i in range(len(tabla)):
        for j in range(len(tabla[0])):
            if tabla[i][j] == 0:
                return(i, j) #sor, oszlop
    return None


print_tabla(tablazat)
print()
megold(tablazat)
print()
print_tabla(tablazat)
