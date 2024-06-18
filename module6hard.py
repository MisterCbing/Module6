import math

class Figure():
    sides_count = 0
    def __is_valid_sides(self, __sides):
        if len(list(__sides)) == self.sides_count:
            return True

    def __init__(self, __color, *__sides, filled = False):
        self.__color = __color
        self.filled = filled
        self.__sides = list(__sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, __color):
        if all(map(lambda x: 0 <= x <= 255, __color)):
            return True

    def set_color(self, *__color):
        if self.__is_valid_color(__color):
            self.__color  = __color

    def set_sides(self, *__sides):
        if self.__is_valid_sides(__sides):
            self.__sides = __sides

    def get_sides(self):
        return self.__sides

    def len(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def len(self):
        return self._Figure__sides[0] * 2 * math.pi

class Triangle(Figure):
    sides_count = 3

class Cube(Figure):
    sides_count = 12
    def get_sides(self):
        return self._Figure__sides * self.sides_count

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_sides())