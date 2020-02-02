class Matrix:
    def __init__(self):
        self.string = None
        self.column = None
        self.mat = []

    def input_mat(self):
        self.string = int(input('Строки: '))
        self.column = int(input('Столбцы: '))
        self.mat = [[int(input('Элементы: ')) for x in range(self.column)]
                    for x in range(self.string)]

    def out_mat(self):
        for x in self.mat:
            print(x)


m = Matrix()
m.input_mat()
m.out_mat()
