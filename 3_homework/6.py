from math import sqrt


def sort_4isla(x):
    for i in range(2, int(sqrt(x))+1):
        if not x % i:
            return False
        return True


enter = int(input())
print(sort_4isla(enter))
