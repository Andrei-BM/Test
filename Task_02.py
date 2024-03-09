""" Функция для вычисления площади круга и треугольника
на вход ожидается получить цифры разделенные пробелом. В зависимости от количества введенных
цифр функция определяет тип фигуры. """


def calc_area(*args):
    if len(args) == 1:
        Circle(args)
    elif len(args) == 3:
        Triangle(sorted(args, reverse=True))
    else:
        print('Другие возможности пока в разработке.')


class Circle:
    # Класс для расчета площади круга

    def __init__(self, data: tuple):
        from math import pi
        self.name = 'круг'
        self.radius = data[0]
        self.pi = pi
        # Проверяем данные
        if self.radius > 0:
            # Получаем словарь с данными
            self.data = self.calc()
            # Выводим на экран
            self.report()
        else:
            # В случе ошибки
            self.false_report()

    def calc(self):

        data = dict()
        data['Площадь'] = round(self.pi * pow(self.radius, 2), 2)
        data['Диаметр'] = 2 * self.radius

        return data

    def report(self):
        print(f'Фигура - {self.name}: ')
        for key, value in self.data.items():
            print(f'\t{key} - {value}')

    @staticmethod
    def false_report():
        print('Такая фигура невозможна.')


class Triangle(Circle):

    def __init__(self, data: tuple):
        self.name = 'треугольник'
        self.a = data[0]
        self.b = data[1]
        self.c = data[2]
        self.special = None
        # Проверяем возможность существования
        self.possible = self.check()
        if self.possible:
            # Получаем словарь с данными
            self.data = self.calc()
            self.report()
        else:
            self.false_report()

    def check(self):
        if self.a == self.b == self.c and self.a > 0:
            self.special = 'равносторонний'
            return True
        elif self.a < 0 or self.b < 0 or self.c < 0:
            return False
        elif self.a < self.b + self.c:
            if self.b == self.a or self.b == self.c:
                self.special = 'равнобедренный'
            return True
        else:
            return False

    def calc(self):

        data = dict()
        hp = (self.a + self.b + self.c) / 2
        # Вычисляем площадь по формуле Герона
        area = pow((hp - self.a) * (hp - self.b) * (hp - self.c) * hp, 0.5)
        data['Площадь'] = round(area, 2)
        # Вычисляем площадь по формуле для прямоугольного треугольника и проверяем на равенство
        check_special = round(0.5 * self.b * self.c, 2)
        if not self.special and data['Площадь'] == check_special:
            self.special = 'прямоугольный'
        data['Особенность'] = self.special
        return data


if __name__ == '__main__':
    calc_area(3)
    calc_area(5, 4, 3)
