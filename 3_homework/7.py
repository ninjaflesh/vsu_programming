enter = input("Vvod: ").split()

m = list(map(len, enter))
print(enter[m.index(max(m))])

m.clear()
m = [enter.count(x) for x in set(enter)]

print(list(set(enter))[m.index(max(m))])
