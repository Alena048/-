from abc import ABC, abstractmethod
import json
import pickle
class Shape:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        pass

    @classmethod
    def valid_str(cls, data):
        if not isinstance(data, str):
            raise TypeError("Должна быть введена строка")

    @classmethod
    def valid_int(cls, data):
        if not isinstance(data, int):
            raise TypeError("Должны быть введена цифры")

    @abstractmethod
    def save(self):
        pass

    @staticmethod
    def load(path: str):
        with open(path, "r") as read_file:
            data = json.load(read_file)
            print(data)
            return data

class Square(Shape):
    def __init__(self, left_corner: int, length: int, name: str = "Квадрат"):
        super().__init__(name=name)
        self.valid_int(left_corner)
        self.valid_int(length)

        self.left_corner = left_corner
        self.length = length

    def __str__(self):
        return f'Фигура {self.name}\nКоординаты левого верхнего угла: {self.left_corner}\nДлина сторон: {self.length}\n'

    def save(self, path: str):
        self.valid_str(path)
        with open(path, "w") as write_file:
            json.dump(self.__dict__, write_file)

    def dictionary(self):
        return self.__dict__

class Rectangle(Shape):
    def __init__(self, left_corner: int, width: int, height: int, name: str = "Прямоугольник"):
        super().__init__(name=name)
        self.valid_int(left_corner)
        self.valid_int(width)
        self.valid_int(height)

        self.left_corner = left_corner
        self.width = width
        self.height = height

    def __str__(self):
        return f'Фигура {self.name}\nКоординаты левого верхнего угла: {self.left_corner}\nШирина: {self.width}\nВысота: {self.height}\n'

    def save(self, path: str):
        self.valid_str(path)
        with open(path, "w") as write_file:
            json.dump(self.__dict__, write_file)

    def dictionary(self):
        return self.__dict__

class Circle(Shape):
    def __init__(self, centr: int, radius: int, name: str = "Круг"):
        super().__init__(name=name)
        self.valid_int(centr)
        self.valid_int(radius)

        self.centr = centr
        self.radius = radius

    def __str__(self):
        return f'Фигура {self.name}\nКоордината центра: {self.centr}\nКоордината радиуса{self.radius}\n'

    def save(self, path: str):
        self.valid_str(path)
        with open(path, "w") as write_file:
            json.dump(self.__dict__, write_file)

    def dictionary(self):
        return self.__dict__

class Ellipse(Shape):
    def __init__(self, top_corner: int, width: int, height: int, parallel_axis: int, name: str = "Эллипс"):
        super().__init__(name=name)
        self.valid_int(top_corner)
        self.valid_int(width)
        self.valid_int(height)
        self.valid_int(parallel_axis)

        self.top_corner = top_corner
        self.width = width
        self.height = height
        self.parallel_axis = parallel_axis

    def __str__(self):
        return f'Фигура {self.name}\nВерхний угол: {self.top_corner}\nШирина: {self.width}\nВысота: {self.height}\nПараллельная ось: {self.parallel_axis}\n'

    def save(self, path: str):
        self.valid_str(path)
        with open(path, "w") as write_file:
            json.dump(self.__dict__, write_file)

    def dictionary(self):
        return self.__dict__



square = Square(90, 8)
print(square.__str__())
square.save("square.json")
square.load("square.json")

rectangle = Rectangle(90, 65,78)
print(rectangle.__str__())
rectangle.save("rectangle.json")
rectangle.load("rectangle.json")

circle = Circle(7, 9)
print(circle.__str__())
circle.save("circle.json")
circle.load("circle.json")

ellips = Ellipse(87, 67, 90, 5)
print(ellips.__str__())
ellips.save("ellips.json")
ellips.load("ellips.json")
#
#
list_shape = []
list_shape.append(ellips)
list_shape.append(circle)
list_shape.append(rectangle)
list_shape.append(square)
# print(list_shape)


with open("my_dict.pkl", "wb") as f:
    pickle.dump(list_shape, f)

with open("my_dict.pkl", "rb") as f:
    loaded_dict = pickle.load(f)
print(loaded_dict)