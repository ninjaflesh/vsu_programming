def sort_4isla(x):
    if x == 2 or x == 3 or x == 5 or x == 7:
        return True
    return bool(x % 7 and x % 5 and x % 3 and x % 2)


enter = int(input())
print(sort_4isla(enter))
