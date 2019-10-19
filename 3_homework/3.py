def fib_print(inp):
    feb = [0, 1]
    for i in range(inp - 2):
        feb.append(feb[-1] + feb[-2])
    print(feb)


enter = int(input("Enter Fib num: "))
fib_print(enter)
