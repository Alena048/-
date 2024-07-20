# Задача 1 и 2
#
# from abc import ABC, abstractmethod
#
# class Figure:
#     def __init__(self, name: str):
#         self.valid_str(name)
#         self.name = name
#
#     def __str__(self):
#         print(f'Площадь {self.name}: {self.area()}')
#
#     def __int__(self):
#         return self.area()
#
#     @classmethod
#     def valid_int(cls, data: int):
#         if not isinstance(data, int):
#             raise TypeError("Необходимо вводить только цифры")
#
#     @classmethod
#     def valid_str(cls, data: str):
#         if not isinstance(data, str):
#             raise TypeError("Необходимо вводить строку")
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Rectangle(Figure):
#     def __init__(self, height: int, width: int, name: str = "Прямоугольник"):
#         super().__init__(name)
#         self.valid_int(height)
#         self.valid_int(width)
#
#         self.height = height
#         self.width = width
#
#     def area(self):
#         area_rectangle = self.height*self.width
#         return area_rectangle
#
#     def __str__(self):
#         super().__str__()
#         return f'Ширина {self.width}, высота {self.height} \n'
#
#
#
# class Circle(Figure):
#     def __init__(self, radius: int, name: str = "Круг"):
#         super().__init__(name)
#         self.valid_int(radius)
#
#         self.radius = radius
#
#     def area(self):
#         pi = 3.14
#         radius_st = pow(self.radius, 2)
#         area_circle = pi*radius_st
#         # return round(area_circle)
#         return area_circle
#
#     def __str__(self):
#         super().__str__()
#         return f'Радиус круга равен {self.radius} \n'
#
#
#
# class Right_triangle(Figure):
#     def __init__(self, katet_1: int, katet_2: int):
#         super().__init__("Прямоугольный треугольник")
#         self.valid_int(katet_1)
#         self.valid_int(katet_2)
#
#         self.katet_1 = katet_1
#         self.katet_2 = katet_2
#
#     def area(self):
#         area_right = (self.katet_1*self.katet_2)/2
#         return area_right
#
#     def __str__(self):
#         super().__str__()
#         return f'Длина первая равна: {self.katet_1}, длина вторая равна: {self.katet_2} \n'
#
#     def __int__(self):
#         return self.area()
#
# class Trapezoid(Figure):
#     def __init__(self, base_1: int, base_2: int, height: int, name: str = "Трапеция"):
#         super().__init__(name)
#         self.valid_int(base_1)
#         self.valid_int(base_2)
#         self.valid_int(height)
#
#         self.base_1 = base_1
#         self.base_2 = base_2
#         self.height = height
#
#     def area(self):
#         area_trapez = (self.base_1+self.base_2)/2*self.height
#         return area_trapez
#
#     def __str__(self):
#         super().__str__()
#         return f'Основание первое: {self.base_1}, основание второе: {self.base_2}, высота: {self.height} \n'
#

# x = Rectangle(5, 8)
# print(x.area())
# print(x.__str__())
# print(x.__int__())
#
# y = Circle(7)
# print(y.area())
# print(y.__str__())
# print(y.__int__())
#
# z = Right_triangle(6, 9)
# print(z.area())
# print(z.__str__())
# print(z.__int__())
#
# q = Trapezoid(10, 6, 8)
# print(q.area())
# print(q.__str__())
# print(q.__int__())

# Вариант вывода результатов через цикл
# while True:
#     print("1. Прямоугольник")
#     print("2. Круг")
#     print("3. Прямоугольный треугольник")
#     print("4. Трапеция")
#     print("5. Выход")
#     vibor = int(input("Введите номер фигуры для расчета площади: \n"))
#     if vibor == 1:
#         height = int(input("Введите высоту прямоугольника \n"))
#         width = int(input("Введите ширину прямоугольника \n"))
#         rectangle = Rectangle(height, width)
#         print(rectangle.__str__())
#     elif vibor == 2:
#         radius = int(input("Введите радиус круга: \n"))
#         circle = Circle(radius)
#         print(circle.__str__())
#     elif vibor == 3:
#         katet_1 = int(input("Введите первую длину стороны треугольника: \n"))
#         katet_2 = int(input("Введите вторую длину стороны треугольника: \n"))
#         right_triangle = Right_triangle(katet_1, katet_2)
#         print(right_triangle.__str__())
#     elif vibor == 4:
#         base_1 = int(input("Введите первое основание трапеции: \n"))
#         base_2 = int(input("Введите второе основание трапеции: \n"))
#         height = int(input("Введите высоту трапеции: \n"))
#         trapezoid = Trapezoid(base_1, base_2, height)
#         print(trapezoid.__str__())
#     elif vibor == 5:
#         break

