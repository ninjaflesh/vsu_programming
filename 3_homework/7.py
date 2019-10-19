enter = input("Vvod: ").split()

m = list(map(len, enter))
print(enter[m.index(max(m))])

m.clear()
# m = [x for x in (set(enter))]
for x in set(enter):
    m.append(enter.count(x))

print(list(set(enter))[m.index(max(m))])
