s = []
lul = input("Vvod: ")
while lul:
    s.append(lul)
    lul = input("Vvod: ")
s = "".join(sorted(s)[::-1])
print(s)
