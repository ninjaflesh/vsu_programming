class Date:
    def __init__(self):
        self.year = None
        self.month = None
        self.day = None

    def date_enter(self):
        self.year = input('Year: ')
        self.month = input('Month: ')
        self.day = input('Day: ')

    def date_print(self):
        print(f'{self.year}.{self.month}.{self.day}')


d = Date()
d.date_enter()
d.date_print()
