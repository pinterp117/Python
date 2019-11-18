from random import randrange


def value_sum(dic):
    if sum(dic.values()) > 2:
        print("The lamp is on!")
    else:
        print("The lamp is off!")


dic = {"A": None, "B": None, "C": None, "D": None}
question = input("Do you want to specify the order of switches and their state? (yes/no) ")

if question == "no":
    for i in dic.keys():
        dic[i] = randrange(2)
        print("{} is {}-{}".format(i, dic[i], "on" if dic[i] == 1 else "off"))
    value_sum(dic)

if question == "yes":
    sorrend = input("What should be the switches(A B C D) order: ")
    lista = sorrend.split()
    for i in lista:
        if i not in ('A', 'B', 'C', 'D'):
            print("Not correct switches: A B C D are the options")
            exit()
    print("Switches order is: ")
    print(lista)
    for i in lista:
        a = int(input("{} switch (1-on, 0-off): ".format(i)))
        if a in range(0, 2):
            dic[i] = a
        else:
            print("The switch {} status should be 1-on or 0-off.".format(i))
            exit()
    value_sum(dic)

else:
    exit()
