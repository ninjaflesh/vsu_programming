def skobki(r):
    ot = 0
    zk = 0
    ot = r.count("(")
    zk = r.count(")")
    if ot > zk:
        return("Не хватает 1 закрывающей скобки!")
    elif ot < zk:
        return("Не хватает 1 открывающей скобки!")
    else:
        return("Каеф!")


lul = input("Vvod: ")
otv = skobki(lul)
print(otv)
