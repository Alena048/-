# Задача 1
# class Avto:
#     def __init__(self, model: str, year: int, manufacturer: str, volume: int, color: str, price: int):
#         self.__model = model
#         self.__year = year
#         self.__manufacturer = manufacturer
#         self.__volume = volume
#         self.__color = color
#         self.__price = price
#
#     def __str__(self):
#         return (f"Модель автомобиля: {self.__model} \nГод выпуска: {self.__year} \n"
#                 f"Производитель {self.__manufacturer}\nОбъем двигателя: {self.__volume} \n"
#                 f"Цвет автомобиля: {self.__color} \nЦена автомобиля: {self.__price} \n")
#
#     def model(self):
#         return f"Модель автомобиля: {self.__model} \n"
#
#     def year(self):
#         return f"Год выпуска: {self.__year} \n"
#
#     def manufacturer(self):
#         return f"Производитель: {self.__manufacturer} \n"
#
#     def volume(self):
#         return f"Объем двигателя: {self.__volume} \n"
#
#     def color(self):
#         return f"Цвет автомобиля: {self.__color} \n"
#     def set_cf(self, data):
#         self.ff = data
#     def price(self):
#         return f"Цена автомобиля: {self.__price} \n"
#
#     def new_volume(self, new_volume: int):
#         if not isinstance(new_volume, int):
#             raise TypeError("Должно быть числовое значение")
#         self.__volume = new_volume
#
#     def new_color(self, new_color: str):
#         if not isinstance(new_color, str):
#             raise TypeError("Должна быть строка")
#         self.__color = new_color
#
#     def new_price(self, new_price: int):
#         if not isinstance(new_price, int):
#             raise TypeError("Должно быть числовое значение")
#         self.__price = new_price
#
# avto = Avto("Форд", 2020, "Завод", 21, "Белый", 2345678)
# print(avto)
# print(avto.model())
# print(avto.price())
# avto.new_price(999)
# print(avto)

# Задача 2
# class Book:
#
#     def __init__(self, name: str, year: int, publisher: str, genre: str, autop: str, price: int):
#         if not isinstance(name, str):
#             raise TypeError("Должна быть строка")
#         if not isinstance(year, int):
#             raise TypeError("Должно быть числовое значение")
#         if not isinstance(publisher, str):
#             raise TypeError("Должна быть строка")
#         if not isinstance(genre, str):
#             raise TypeError("Должна быть строка")
#         if not isinstance(autop, str):
#             raise TypeError("Должна быть строка")
#         if not isinstance(price, int):
#             raise TypeError("Должно быть числовое значение")
#         self.__name = name
#         self.__year = year
#         self.__publisher = publisher
#         self.__genre = genre
#         self.__autop = autop
#         self.__price = price
#
#     def __str__(self):
#         return f"Название книги: {self.__name} \nГод выпуска: {self.__year} \nИздатель: {self.__publisher} \nЖанр: {self.__genre} \nАвтор: {self.__autop} \nЦена: {self.__price}\n"
#
#     def name_book(self):
#         return f"Название книги: {self.__name} \n"
#
#     def year_book(self):
#         return f"Год выпуска книги {self.__name}: {self.__year} \n"
#
#     def publisher_book(self):
#         return f"Издатель книги {self.__name}: {self.__publisher} \n"
#
#     def genre_book(self):
#         return f":Жанр книги {self.__name}: {self.__genre} \n"
#
#     def autop_book(self):
#         return f"Автор книги {self.__name}: {self.__autop} \n"
#
#     def price_book(self):
#         return f"Цена книги {self.__name}: {self.__price} \n"
#
#     def new_name(self, new_name: str):
#         if not isinstance(new_name, str):
#             raise TypeError("Должна быть строка")
#         self.__name = new_name
#
#     def new_year(self, new_year: int):
#         if not isinstance(new_year, int):
#             raise TypeError("Должно быть числовое значение")
#         self.__year = new_year
#
#     def new_publisher(self, new_publisher: str):
#         if not isinstance(new_publisher, str):
#             raise TypeError("Должна быть строка")
#         self.__publisher = new_publisher
#
#     def new_genre(self, new_genre: str):
#         if not isinstance(new_genre, str):
#             raise TypeError("Должна быть строка")
#         self.__genre = new_genre
#
#     def new_autop(self, new_autop: str):
#         if not isinstance(new_autop, str):
#             raise TypeError("Должна быть строка")
#         self.__autop = new_autop
#
#     def new_price(self, new_price: int):
#         if not isinstance(new_price, int):
#             raise TypeError("Должно быть числовое значение")
#         self.__price = new_price
#
# book = Book("Шантарам", 2020, "Азбука", "Роман", "Г.Д.Робертс", 500)
# print(book)
# print(book.autop_book())
# book.new_price(999)
# print(book)

# Задача 3
# from datetime import datetime
# class Stadium:
#
#     def __init__(self, name: str, opening_date: datetime, country: str, city: str, capacity: int):
#         self.__name = name
#         self.__opening_date = opening_date
#         self.__country = country
#         self.__city = city
#         self.__capacity = capacity
#
#     def __str__(self):
#         return f"Наименование стадиона: {self.__name} \nДата открытия: {self.__opening_date} \nСтрана: {self.__country} \nГород: {self.__city} \nВместимость: {self.__capacity} \n"
#
#     def name_stadium(self):
#         return f"Наименование стадиона: {self.__name} \n"
#
#     def date(self):
#         return f"Дата открытия стадиона {self.__name}: {self.__opening_date} \n"
#
#     def country(self):
#         return f"Страна, в которой находится стадион {self.__name}: {self.__country} \n"
#
#     def city(self):
#         return f"Город, в котором находится стадион {self.__name}: {self.__city} \n"
#
#     def capacity(self):
#         return f"Вместимость стадиона {self.__name}: {self.__capacity} \n"
#
#     def new_name(self, new_name: str):
#         if not isinstance(new_name, str):
#             raise TypeError("Должна быть строка")
#         self.__name = new_name
#
#     def new_capacity(self, new_capacity: int):
#         if not isinstance(new_capacity, int):
#             raise TypeError("Должно быть числовое значение")
#         self.__capacity = new_capacity
#
# stadium = Stadium("Камп Ноу", datetime(1957, 9, 24), "Испания", "Барселона", 99354 )
# print(stadium)
# print(stadium.capacity())
# print(stadium.country())
# stadium.new_capacity(10000000)
# print(stadium)