# Декораторы
import datetime
from time import sleep, time

a = 1
def my_decorator(func):
    def wrapper(*args, **kwargs):
        duration_start = time()
        func(*args, **kwargs)
        duration_end = time()
        result = duration_end - duration_start
        print(f"Тест выполнился за {float(result)}")
    return wrapper

@my_decorator
def my_test_func():
    print("Тест выполнен")
    sleep(1.2)

my_test_func()
a = 1
def repeat(num: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(num=3)
def sum_int(*args):
    return print(sum(args))

sum_int(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Метод класса (@classmethod) и (@staticmethod)

# class Car:
#     car_count = 0
#
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         Car.car_count += 1
#
#     @classmethod
#     def from_string(cls, car_str):
#         # Альтернативный конструктор, создающий объект из строки "Brand-Model"
#         brand, model = car_str.split("-")
#         return cls(brand, model)
#
# # car1 = Car.from_string("Toyota-Corolla")
# # print(f"Бренд: {car1.brand}, Модель: {car1.model}")
# # print(f"Всего автомобилей: {Car.car_count}")
# # car2 = Car("a" , "n")
#
#
# class Employee:
#     company = "TechCorp"  # обычный атрибут класса (общая для всех объектов)
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def display_info(self):
#         # Обычный метод - работает с конкретным объектом (self)
#         print(f"{self.name} зарабатывает {self.salary} в компании {self.company}")
#
#     @classmethod
#     def change_company(cls, new_company):
#         # Метод класса - работает с классом в целом (cls)
#         cls.company = new_company
#         print(f"Название компании изменено на: {new_company}")
#
#
#     @classmethod
#     def from_string(cls, employee_string):
#         # Ещё один полезный пример - альтернативный конструктор
#         name, salary = employee_string.split("-")
#         return cls(name, int(salary))
#
#     @staticmethod
#     def validate_data(employee_string):
#         return len(employee_string.split("-")) == 2
#
# def create(employee_string):
#     if Employee.validate_data(employee_string):
#         return Employee.from_string(employee_string)
#     else:
#         return print("данные кривые")
#
#
#
# # emp1 = Employee("Иван", 50000)
# # emp1.display_info()
# # emp2 = Employee("Мария", 60000)
# # emp2.display_info()
# #
# # Employee.change_company("NewTech")
# #
# # emp1.display_info()
# # emp2.display_info()
# #
# # emp3 = Employee.from_string("Петр-70000")
# # emp3.display_info()
#
# print(Employee.validate_data("Петр-70000-100"))
# emp5 = create("Петр-70000-100")
#
# # Свойства класса (@property)
# class NewCar:
#     def __init__(self, brand, model, speed_car=0):
#         self.brand = brand
#         self.model = model
#         self.__speed = speed_car  # Приватный атрибут скорости
#
#     @property
#     def speed(self):
#         """Геттер для получения скорости автомобиля."""
#         return self.__speed
#
#     @speed.setter
#     def speed(self, value):
#         """Сеттер с проверкой диапазона значений."""
#         if value < 0:
#             print("Ошибка: скорость не может быть отрицательной!")
#         elif value > 300:
#             print("Ошибка: превышено максимально допустимое значение скорости (300 км/ч)!")
#         else:
#             self.__speed = value
#
#     @speed.deleter
#     def speed(self):
#         print("Скорость сброшена")
#         self.__speed = "Скорость отсуствует, требуетс установка этого значения"
#
# car1 = NewCar("Tesla", "Model S", 250)
# print(car1.speed)
# car1.speed = 300
# print(car1.speed)
# del car1.speed
# print(car1.speed)
