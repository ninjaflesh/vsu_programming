from random import randint
rand = randint(0, 100)
s = int(input("Vvod: "))
while s != rand:
    if s > rand:
        print("Загаданное число меньше!")
    else:
        print("Загаданное число больше!")
    s = int(input("Vvod: "))
print("Вы угадали число!")
