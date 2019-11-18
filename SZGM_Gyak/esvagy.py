tomb = []
for i in range(4):
    all = int(input("A kapcsoló állapota (1-fel, 0-le): "))
    tomb.append(all)
if sum(tomb) >= 3:
    print("Ég a lámpa")
else:
    print("Nem ég a lámpa")