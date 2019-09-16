x = input('Vvod x: ')
y = input('Vvod x: ')
x = float(x)
y = float(y)
if x > 0 and y > 0:
    print('1 4etvert')
elif x < 0 and y > 0:
    print('2 4etvert')
elif x < 0 and y < 0:
    print('3 4etvet')
elif x > 0 and y < 0:
    print('4 4etvert')
elif not x or not y:
    print('na osi')
