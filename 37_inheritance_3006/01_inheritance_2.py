"""
Виды наследования:
1. Простое наследование дочерним классом атрибутов родительского класса
2. Полное переопределение в дочернем классе некоторых методов родителя
3(!!!). Расширение в дочернем классе методов родителя
"""


class Table:  # базовый класс
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class WorkTable(Table):  # класс WorkTable наследуется от класса Table
    def square(self):
        return self.width * self.length


class ComputerTable(WorkTable):
    def square(self, monitor):
        return self.width * self.length - monitor



t1 = Table(100, 80, 80)
t2 = WorkTable(120, 100, 85)
t3 = ComputerTable(120, 100, 85)
print('площадь рабочего стола', t2.square())
print('площадь компьютерного стола с монитором площадью 20', t3.square(20))




