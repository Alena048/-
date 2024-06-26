# Задача №2
# class Temperature:
#
#     count = 0
#
#     def __init__(self, celsius: int, fahrenheit: int):
#         self.valid_celsius(celsius)
#         self.valid_fahrenheit(fahrenheit)
#
#         self.celsius = celsius
#         self.fahrenheit = fahrenheit
#
#     def __str__(self):
#         return f"Температура Цельсий: {self.celsius}, температура Фарингейт: {self.fahrenheit}"
#
#     @classmethod
#     def valid_celsius(cls, celsius: int):
#         if not isinstance(celsius, int):
#             raise TypeError("Вводить только цифры")
#
#     @classmethod
#     def valid_fahrenheit(cls, fahrenheit: int):
#         if not isinstance(fahrenheit, int):
#             raise TypeError("Вводить только цифры")
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius: int):
#         Temperature.valid_celsius(celsius)
#         Temperature.count += 1
#         calculation = (celsius * 1.8) +32
#         return f"Температура по Фарингейту составляет: {calculation}"
#
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit: int):
#         Temperature.valid_fahrenheit(fahrenheit)
#         Temperature.count += 1
#         calculation1 = round((fahrenheit - 32) / 1.8)
#         return f"Температура по Цельсию составляет: {calculation1}"
#
#     @staticmethod
#     def tem_count():
#         return f"Количество расчетов температуры: {Temperature.count}"
#
#
# temper = Temperature
# print(temper.fahrenheit_to_celsius(74))
# print(temper.celsius_to_fahrenheit(32))
# print(temper.fahrenheit_to_celsius(55))
# print(temper.celsius_to_fahrenheit(23))
# print(temper.tem_count())


# Задача №3

# class Translation:
#     @classmethod
#     def valid_data(cls, data: int):
#         if not isinstance(data, int):
#             raise TypeError("Вводить только цифры")
#
#     @staticmethod
#     def metre_to_yard(metre: int, yard: int):
#         Translation.valid_data(metre)
#         Translation.valid_data(yard)
#         result_yard = metre*1.0936
#         result_metre = yard*0.9144
#         return f"{metre} метра = {result_yard} ярда \n{yard} ярда = {result_metre} метра"
#
#     @staticmethod
#     def centimetre_inch(centimetre: int, inch: int):
#         Translation.valid_data(centimetre)
#         Translation.valid_data(inch)
#         result_inch = centimetre*0.39
#         result_centimetre = inch*2.54
#         result_inch1 = round(result_inch, 2)
#         return f"{centimetre} сантиметр = {result_inch1} дюйм \n{inch} дюйм = {result_centimetre} сантиметр"
#
#     @staticmethod
#     def kilometer_to_mile(kilometer: int, mile: int):
#         Translation.valid_data(kilometer)
#         Translation.valid_data(mile)
#         result_mile = kilometer*0.62137
#         result_kilometre = mile*1.60934
#         return f"{kilometer} километр = {result_mile} миль \n{mile} миль = {result_kilometre} километров"
#
#     @staticmethod
#     def millimeter_to_inch(millimeter: int, inch: int):
#         Translation.valid_data(millimeter)
#         Translation.valid_data(inch)
#         result_inch = millimeter*0.0393701
#         result_millimetre = inch*25.4
#         result_inch1 = round(result_inch, 2)
#         result_millimetre1 = round(result_millimetre, 2)
#         return f"{millimeter} миллиметр = {result_inch1} дюйм \n{inch} дюйм = {result_millimetre1} миллиметров"
#
# calculator = Translation
# print(calculator.metre_to_yard(6, 6))
# print(calculator.centimetre_inch(6, 6))
# print(calculator.kilometer_to_mile(3, 3))
# print(calculator.millimeter_to_inch(3, 3))