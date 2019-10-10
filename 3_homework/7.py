enter = input("Vvod: ").split()
m = list(map(lambda s: len(s), enter))
print(enter[m.index(max(m))])
one = set(enter)
m.clear()
for x in one:
    m.append(enter.count(x))
print(list(one)[m.index(max(m))])
