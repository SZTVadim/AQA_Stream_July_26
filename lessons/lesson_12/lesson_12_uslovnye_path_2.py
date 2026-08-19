# Цикл while
# a = 1
# while True:
#     value = input("Enter a number: ")  # ввод инпута это str
#     if value.isdigit():
#         if int(value) == 665:
#             print("Вы угадали")
#             break


# number = 1
# while number < 5:
#     print(f"number = {number}")
#     number += 1
# print("Работа программы завершена")

# Цикл for
# message = "Hello_ _World"
# for i in message:
#     print(i)

# for c range
# for n in range(10):
#     print(n)

# range может задаваться тремя параметрами (start, stop, step),
# если передали один то это значит начинаем с 0 и заканчиваем переданным значением - 1

# for n in range(3, 102, 3):
#     print(n)

# Цикл for … else
# response_json = [
#   {"id": 10, "name": "Ann", "active": True},
#   {"id": 42, "name": "Ivan", "active": True},
#   {"id": 7, "name": "Kate", "active": False}
# ]
# for item in response_json:
#     if item["id"] == 43:
#         assert item["active"] is True
#         print("Found")
#         break
# else:
#     print("person with id 42 Not Found")

# Анонимные функции (lambda)
# пример без анонимной функции
# def my_func(x):
#     return x ** 2
#
# print(my_func(4))
#
# пример с анонимной функции
# square_func = lambda any_int: any_int ** 2
# print(square_func(66))

people = [("Вася", 52), ("Петя", 12), ("Таня", 32)]
new_list = sorted(people, key=lambda x: x[1])
print(new_list)