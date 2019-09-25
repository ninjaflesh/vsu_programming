lul = input("Vvod: ")
ot = 0
zk = 0
for x in lul:
    if x == "(":
        ot += 1
    elif x == ")":
        zk += 1
if ot > zk:
    print("Не хватает 1 закрывающей скобки!")
elif ot < zk:
    print("Не хватает 1 открывающей скобки!")
else:
    print("Каеф!")
