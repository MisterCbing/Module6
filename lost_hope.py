import math

class Figure():
    sides_count = 0
    def __is_valid_sides(self, __sides):
        if len(list(__sides)) == self.sides_count:
            return True

    def __init__(self, __color, *__sides, filled = False):
        self.__color = list(__color)
        self.filled = filled
        self.__sides = list(__sides)
        # if self.__is_valid_sides(__sides):
        #     self.__sides = list(__sides)
        # else:
        #     self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, __color):
        if all(map(lambda x: 0 <= x <= 255, __color)):
            return True

    def set_color(self, *__color):
        if self.__is_valid_color(__color):
            self.__color  = list(__color)

    def set_sides(self, *__sides):
        if self.__is_valid_sides(__sides):
            self.__sides = list(__sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides, filled = False):
        super().__init__(__color, *__sides, filled = False)
        self.__color = list(__color)
        self.filled = filled
        self.__sides = list(__sides)
        if len(self.__sides) > 1:
            self.__sides = [1]
        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return self.__radius ** 2 * math.pi

    def set_sides(self, *__sides):
        self.__sides = list(__sides)

    def __len__(self):
        return sum(self.__sides)

    def get_sides(self):
        return self.__sides

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        return (self.pp * (self.pp - self.__sides[0]) * (self.pp - self.__sides[1]) *(self.pp - self.__sides[2])) ** 0.5
    def __init__(self, __color, *__sides, filled=False):
        super().__init__(__color, *__sides, filled=False)
        self.__color = list(__color)
        self.filled = filled
        self.__sides = list(__sides)
        if len(self.__sides) != 3:
            self.__sides = [1] * self.sides_count
        self.pp = sum(self.__sides) / 2
        self.sq = self.get_square()
        self.__height = self.sq / self.__sides[0] * 2

    def get_sides(self):
        return self.__sides

    def get_height(self):
        return self.__height

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, *__sides, filled = False):
        super().__init__(__color, *__sides, filled = False)
        self.__color = list(__color)
        self.filled = filled
        self.__sides = list(__sides)
        if len(self.__sides) == 1:
            self.__sides = self.__sides * self.sides_count
        else:
            self.__sides = [1] * self.sides_count

    def get_sides(self):
        return self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
cube1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

