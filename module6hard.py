class Figure():
    sides_count = 0

    def __init__(self, __color, __sides, filled = False):
        self.__color = __color
        self.__sides = __sides
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, __color):
        if all(map(lambda x: 0 <= x <= 255, __color)):
            return True

    def set_color(self, *__color):
        if self.__is_valid_color(__color):
            self.__color  = __color

class Circle(Figure):
    sides_count = 1

class Triangle(Figure):
    sides_count = 3

class Cube(Figure):
    sides_count = 12

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())