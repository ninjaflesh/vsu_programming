def Fib_print(inp):
    feb = [0, 1]
    for i in range(inp - 2):
        last = feb[len(feb) - 1]
        first = feb[len(feb) - 2]
        feb.append(last + first)
    print(last + first)
    print(feb)


enter = int(input("Enter Fib num: "))
Fib_print(enter)
