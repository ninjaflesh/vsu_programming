x = input('Vvod x: ')
y = input('Vvod x: ')
x = int(x)
y = int(y)
counter = 0
for x in range(x, y + 1, 1):
    if not x % 5:
        counter += x
print(counter)
