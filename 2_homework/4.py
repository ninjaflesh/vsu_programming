def skobki(r):
    ot = 0
    zk = 0
    for x in r:
        if x == "(":
            ot += 1
        elif x == ")":
            zk += 1
    if ot > zk:
        return("Не хватает 1 закрывающей скобки!")
    elif ot < zk:
        return("Не хватает 1 открывающей скобки!")
    else:
        return("Каеф!")


lul = input("Vvod: ")
otv = skobki(lul)
print(otv)
