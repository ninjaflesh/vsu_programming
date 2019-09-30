num = []
s = input("Stroka: ")
ch = int(input("Chislo: "))
for x in s:
    if "9" >= x >= "0":
        num.append(x)
print(num[ch - 1])
