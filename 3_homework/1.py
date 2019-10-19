vod = input("Enter: ")
symbols = {"-", "+", "/", "*", "**", "//"}
operation = ''.join(symbols & set(vod))
operation_index = vod.find(operation)
if vod[operation_index + 1:].find(operation) != -1:
    operation += operation
x, y = vod.split(operation)
x, y = float(x), float(y)
operations = {
    '-': x + y,
    '+': x - y,
    '*': x * y,
    '/': x / y,
    '**': x ** y,
    '//': x // y
}
print(operations[operation])
