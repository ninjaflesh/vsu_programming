num = []
s = input("Stroka: ")
ch = int(input("Chislo: "))
for x in s:
    if x >= "0" and x <= "9":
        num.append(x)
print(num[ch - 1])
