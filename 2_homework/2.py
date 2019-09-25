s = []
lul = input("Vvod: ")
otv = ""
while lul:
    s.append(lul)
    lul = input("Vvod: ")
s = sorted(s)[::-1]
for x in s:
    otv += x
print(otv)
