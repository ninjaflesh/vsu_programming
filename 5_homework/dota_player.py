from collections import deque


def dota_pleyer(x):
    if not len(x) % 2 and x[0] == "D":
        return True
    return False


name = {
    "Valera": ["Egor", "Karl"],
    "Egor": ["Arsen", "Daha"],
    "Karl": ["Dima", "Ola", "Sveta"]
}

d = deque(name["Valera"])
r = []
while name:
    chelik = d.popleft()
    if chelik not in r:
        if dota_pleyer(chelik):
            print(chelik)
            break
        else:
            d += name.get(chelik, [])
        r.append(chelik)
