spis = []
lul = input("Vvod: ")
while lul:
    spis.append(lul)
    lul = input("Vvod: ")
spis = "".join(sorted(spis, reverse=True))
print(spis)
