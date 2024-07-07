# Задача 1
# class Device:
#     def __init__(self, model: str, brend: str, power: int):
#         self.valid_str(model)
#         self.valid_str(brend)
#         self.valid_int(power)
#
#         self.model = model
#         self.brend = brend
#         self.power = power
#
#     @classmethod
#     def valid_str(cls, data: str):
#         if not isinstance(data, str):
#             raise TypeError("Необходимо вводить только буквы")
#
#     @classmethod
#     def valid_int(cls, data: int):
#         if not isinstance(data, int):
#             raise TypeError("Необходимо вводить только цифры")
#
#     def turn_on(self) -> str:
#         return f'{self.model} {self.brend}: включен'
#
#     def turn_off(self) -> str:
#         return f'{self.model} {self.brend}: выключен \n'
#
#     def info(self) -> str:
#         return f"{self.model} бренд {self.brend} обладает мощностью {self.power}"
#
# class CoffeeMachine(Device):
#     def __init__(self, model: str, brend: str, power: int,  capacity: int):
#         super().__init__(model, brend, power)
#         self.valid_int(capacity)
#
#         self.capacity = capacity
#
#     def info_capacity(self):
#         return f'{self.model} бренд {self.brend}, количествo: {self.capacity} шт'
#
# class Blender(Device):
#
#     def __init__(self, model: str, brend: str, power: int, capacity: int):
#         super().__init__(model, brend, power)
#         self.valid_int(capacity)
#
#         self.capacity = capacity
#
#     def info_capacity(self) -> str:
#         return f'{self.model} бренд {self.brend}, количество: {self.capacity} шт'
#
#
# class MeatGrinder(Device):
#
#     def __init__(self, model: str, brend: str, power: int, capacity: int):
#         super().__init__(model, brend, power)
#         self.valid_int(capacity)
#
#         self.capacity = capacity
#
#     def info_capasity(self) -> str:
#         return f"{self.model} бренд {self.brend}, количество: {self.capacity} шт"
#
#
#
# coffe = CoffeeMachine("Кофемашина", "Ромашка", 786, 1)
# print(coffe.turn_on())
# print(coffe.info())
# print(coffe.info_capacity())
# print(coffe.turn_off())
#
# blender = Blender("Блендер", "Samsung", 789, 2)
# print(blender.turn_on())
# print(blender.info())
# print(blender.info_capacity())
# print(blender.turn_off())
#
# meat = MeatGrinder("Мясорубка", "Samsung", 789, 4)
# print(meat.turn_on())
# print(meat.info())
# print(meat.info_capasity())
# print(meat.turn_off())

# Задача 1 второй вариант
#
# from abc import ABC, abstractmethod
#
# class Device:
#     def __init__(self, model: str, brend: str, power: int):
#         self.valid_str(model)
#         self.valid_str(brend)
#         self.valid_int(power)
#
#         self.model = model
#         self.brend = brend
#         self.power = power
#
#     @classmethod
#     def valid_str(cls, data: str):
#         if not isinstance(data, str):
#             raise TypeError("Необходимо вводить только буквы")
#
#     @classmethod
#     def valid_int(cls, data: int):
#         if not isinstance(data, int):
#             raise TypeError("Необходимо вводить только цифры")
#
#     @abstractmethod
#     def turn_on(self) -> str:
#         pass
#
#     @abstractmethod
#     def turn_of(self) -> str:
#         pass
#
#     @abstractmethod
#     def info(self) -> str:
#         pass
#
#
# class CoffeeMachine(Device):
#     def __init__(self, model: str, brend: str, power: int,  capacity: int):
#         super().__init__(model, brend, power)
#         self.valid_int(capacity)
#
#         self.capacity = capacity
#
#     def turn_on(self) -> str:
#         return f'{self.model} бренд {self.brend}: включена'
#
#     def turn_of(self) -> str:
#         return f'{self.model} бренд {self.brend}: выключена \n'
#
#     def info(self) -> str:
#         return f'{self.model} бренд {self.brend}, мощность {self.power}, количество {self.capacity} шт'
#
# class Blender(Device):
#     def __init__(self, model: str, brend: str, power: int, capacity: int):
#         super().__init__(model, brend, power)
#         self.valid_int(capacity)
#
#         self.capacity = capacity
#
#     def turn_on(self) -> str:
#         return f'{self.model} бренд {self.brend}: включена'
#
#     def turn_of(self) -> str:
#         return f'{self.model} бренд {self.brend}: выключена \n'
#
#     def info(self) -> str:
#         return f'{self.model} бренд {self.brend}, мощность {self.power}, количество {self.capacity} шт'
#
# class MeatGrinder(Device):
#     def __init__(self, model: str, brend: str, power: int, capacity: int):
#         super().__init__(model, brend, power)
#         self.valid_int(capacity)
#
#         self.capacity = capacity
#
#     def turn_on(self) -> str:
#         return f'{self.model} бренд {self.brend}: включена'
#
#     def turn_of(self) -> str:
#         return f'{self.model} бренд {self.brend}: выключена \n'
#
#     def info(self) -> str:
#         return f'{self.model} бренд {self.brend}, мощность {self.power}, количество {self.capacity} шт'
#
#
#
# coffe = CoffeeMachine("Кофемашина", "Ромашка", 786, 1)
# print(coffe.turn_on())
# print(coffe.info())
# print(coffe.turn_of())
#
# blender = Blender("Блендер", "Samsung", 789, 2)
# print(blender.turn_on())
# print(blender.info())
# print(blender.turn_of())
#
# meat = MeatGrinder("Мясорубка", "Samsung", 789, 4)
# print(meat.turn_on())
# print(meat.info())
# print(meat.turn_of())



# Задача 2

# from abc import ABC, abstractmethod
# import math
#
# class Ship:
#
#     def __init__(self, model: str, name: str, power: int):
#         self.valid_str(model)
#         self.valid_int(power)
#         self.valid_str(name)
#
#         self.model = model
#         self.name = name
#         self.power = power
#
#     @classmethod
#     def valid_str(cls, data: str):
#         if not isinstance(data, str):
#             raise TypeError("Необходимо вводить только буквы")
#
#     @classmethod
#     def valid_int(cls, data: int):
#         if not isinstance(data, int):
#             raise TypeError("Необходимо вводить только цифры")
#
#     def info(self):
#         return f'{self.model} {self.name} мощность {self.power}\n'
#     @abstractmethod
#     def speed(self) -> str:
#         pass
#
# class Frigate(Ship):
#     def __init__(self, model: str, name: str, power: int, way: int, time: int):
#         super().__init__(model, name, power)
#
#         self.valid_str(model)
#         self.valid_str(name)
#         self.valid_int(power)
#         self.valid_int(way)
#         self.valid_int(time)
#
#         self.way = way
#         self.time = time
#
#     def speed(self) -> str:
#         result_speed = self.way / self.time
#         return f'Скорость {self.model} {self.name} равна {math.ceil(result_speed)} км/ч\nПройденное расстояние {self.way} км\nВремя в пути {self.time} ч\n'
#
# class Destroyer(Ship):
#     def __init__(self, model: str, name: str, power: int, way: int, time: int):
#         super().__init__(model, name, power)
#
#         self.valid_str(model)
#         self.valid_str(name)
#         self.valid_int(power)
#         self.valid_int(way)
#         self.valid_int(time)
#
#         self.way = way
#         self.time = time
#
#     def speed(self) -> str:
#         result_speed = self.way / self.time
#         return f'Скорость {self.model} {self.name} равна {math.ceil(result_speed)} км/ч\nПройденное расстояние {self.way} км\nВремя в пути {self.time} ч\n'
#
# class Cruiser(Ship):
#     def __init__(self, model: str, name: str, power: int, way: int, time: int):
#         super().__init__(model, name, power)
#
#         self.valid_str(model)
#         self.valid_str(name)
#         self.valid_int(power)
#         self.valid_int(way)
#         self.valid_int(time)
#
#         self.way = way
#         self.time = time
#
#     def speed(self) -> str:
#         result_speed = self.way / self.time
#         return f'Скорость {self.model} {self.name} равна {math.ceil(result_speed)} км/ч\nПройденное расстояние {self.way} км\nВремя в пути {self.time} ч\n'
#
#
# fregat = Frigate("Фрегат", "Парус", 789, 150, 8)
# print(fregat.speed())
# print(fregat.info())
#
# destroyer = Destroyer("Эсминц", "Победоносец", 1234, 200, 3)
# print(destroyer.speed())
# print(destroyer.info())
#
# cruiser = Cruiser("Крейсер", "Волна", 3456, 247, 7)
# print(cruiser.speed())
# print(cruiser.info())

