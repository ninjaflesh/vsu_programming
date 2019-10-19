from random import randint


def odd_even(data):
    n = len(data)
    is_Sorted = 0
    while is_Sorted:
        is_Sorted = 1
        for i in range(1, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_Sorted = 0
        for i in range(0, n - 1, 2):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                is_Sorted = 0
    return data


rand = [randint(0, 100) for i in range(15)]
print(rand)
odd_even(rand)
print(rand)
