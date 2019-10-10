enter = input("Enter: ")
lst = []
while enter:
    lst.append(enter)
    enter = input("Enter: ")
for i in frozenset(lst):
    print(lst.count(i), i)
