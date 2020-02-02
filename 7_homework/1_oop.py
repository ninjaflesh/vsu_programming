class Matrix:
    def __init__(self):
        self.string = None
        self.column = None
        self.mat = []

    def enter(self):
        self.string = int(input('Строки: '))
        self.column = int(input('Столбцы: '))
        self.mat.append([[input('Элементы: ') for x in range(self.column)]
                         for x in range(self.string)])

    def out(self):
        for x in self.mat:
            for mat in x:
                print(mat)


m = Matrix()
m.enter()
m.out()
