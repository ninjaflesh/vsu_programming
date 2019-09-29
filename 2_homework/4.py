def skobki(r):
    ot = r.count("(")
    zk = r.count(")")
    if ot > zk:
        return("Не хватает" ot-zk "закрывающих скобки!")
    elif ot < zk:
        return("Не хватает" zk-ot "открывающей скобки!")
    return("Каеф!")


lul = input("Vvod: ")
otv = skobki(lul)
print(otv)
