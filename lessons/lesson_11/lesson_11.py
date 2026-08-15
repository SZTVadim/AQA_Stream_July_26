# Функции и условные контрукции в Python
def circle_area(radius):
    pi = 3.14
    result = pi * radius * radius
    return result

# print(circle_area(5))
# print(circle_area(1))
# a = circle_area(5)
# print(a)

# def greeting():
#     print("Hello World")
#
# greeting()
# aa = 1
#
# def divide(a, b):
#     if b == 0:
#         return "На ноль делить нельзя"
#     return a / b
#     print("Hello")
#
# divide(1, 0)
# divide( 0, 1)
#
# result = divide(1, 2)
# print(result)

def add(x: int, y: str):
    return x + int(y)

# позиционные агументы
# print(add(1, "2"))
# print(add("2", 1))  # ошибка в порядке при передаче данных позиционных агументов

# именованные аргументы
# add(x=3, y="4")

# дефолтные аргументы
def greeting(age=None, city=None, name=None):
    if age is not None:
        print(f"мне {age} лет")
    if city:
        print(f"я из города {city}")
    if name:
        print(f"Hello {name}")

greeting(name="Vasya")
greeting(20, "Omsk", "Petya")
greeting()

# произвольное количество аргументов
def all_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

print(all_sum(*range(999999), value=-1))

