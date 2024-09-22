import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple, *sides: int, filled: bool = True):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        self.__color = (r, g, b) \
            if self.__is_valid_color(r, g, b) \
            else self.__color

    def __is_valid_sides(self, sides):
        return (len(sides) == self.sides_count
                and all(side > 0 for side in sides))

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __radius(self):
        return self.__len__() / (2 * math.pi)

    def get_square(self):
        return (self.__len__() ** 2) / (4 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, *__sides)

    def is_valid_triangle(self):  # проверка на невырожденность треугольника
        sides = self.get_sides()  # Т.е. сумма длин любых двух сторон больше длины третьей стороны

        return ((sides[0] + sides[1]) > sides[2]) and ((sides[0] + sides[2]) > sides[1]) and (
                (sides[2] + sides[1]) > sides[0])




def get_square(self):
    a, b, c = self.get_sides()
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides: int, filled: bool = True):
        super().__init__(color, *sides, filled)
        self.__sides = [sides[0]] * self.sides_count

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Выходные данные (консоль):
# [55, 66, 77]
# [222, 35, 130]
# [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
# [15]
# 15
# 216.
