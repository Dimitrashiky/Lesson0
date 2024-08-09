import math
class  Figure:
    sides_count = 0
    def __init__(self, color: tuple[int], sides: tuple[int], filled: bool = True):
        self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

        if not isinstance(self, Cube):
            if len(sides) != self.sides_count:
                self.__sides = [1 for i in range(self.sides_count)]
        else:
            if len(sides) != 1:
                self.__sides = [1]

    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if r < 0 or r > 255:
            return False
        if g < 0 or g > 255:
            return False
        if b < 0 or b > 255:
            return False
        return True
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_sides(self, new_sides: tuple):
        if len(self.__sides) == len(new_sides):
            for side in new_sides:
                if not (side > 0 and isinstance(side, int)):
                    return False
            return True
        return False

    def get_sides(self) -> list:
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if not isinstance(self, Cube):
            if self.sides_count == len(new_sides) and self.__is_valid_sides(new_sides):
                self.__sides = list(new_sides)
        else:
            self.set_cube_sides(new_sides)


    def set_cube_sides(self, new_sides):
        if len(new_sides) == 1:
            if new_sides[0] > 0 and isinstance(new_sides[0], int):
                self.__sides = [new_sides[0] for i in range(self.sides_count)]
        else:
            self.__sides = [1 for i in range(self.sides_count)]


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: list[int], *sides: int, filled: bool = True):
        super().__init__(color, sides, filled)


    def get_square(self):
        self.__radius = self.get_sides()[0] / (2 * math.pi)
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: list[int], *sides: int, filled: bool = True):
        super().__init__(color, sides, filled)

    def get_square(self):
        half_perimetr = len(self) / 2
        self.__square = math.sqrt(half_perimetr * (half_perimetr - self.get_sides()[0]) * (half_perimetr - self.get_sides()[1]) * (half_perimetr - self.get_sides()[2]))
        self.__height = self.__square * 2 / self.get_sides()[0]
        return self.__square

class Cube(Figure):
    sides_count = 12

    def __init__(self, color: list[int], *sides: int, filled: bool = True):
        super().__init__(color, sides, filled)
        self.set_sides(*sides)
    def get_volume(self):
        return self.get_sides()[0] ** 3




circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((222, 35, 130), 4, 5, )

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print(triangle1.get_sides())

[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216








