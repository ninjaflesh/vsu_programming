def season(x):
    sezon = {
        3 <= x <= 5: "Spring",
        6 <= x <= 8: "Summer",
        9 <= x <= 11: "Autemn",
        x == 12 or x <= 2: "Winter"
    }
    return sezon[True]


inp = int(input("Enter month: "))
print(season(inp))
