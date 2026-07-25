# Списки
# my_list_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list_str = ["1", "2", "3", "4", "5"]
# my_list_bool = [True, False]
# my_list_with_list = [[1, 2], [3, [4, 5, [6]]], [7, 8, 9, 10]]
# my_list_obj = [{"age": 22}, {"is_student": True}]

# Добавление элементов
# fruits = ["яблоко"]
# print(fruits)
# fruits.append("банан")
# fruits.append("банан")
# print(fruits)
# fruits.extend(["груша", "апельсин", "mango"])
# print(fruits)
# fruits.insert(2, "виноград")
# print(fruits)

# Удаление элементов
# fruits.remove("груша")
# print(fruits)
# fruits.remove("груша")  # будет ошибка ValueError, так как груши больше нет в списке
# delete_fruit = fruits.pop(2)
# delete_fruit_last = fruits.pop()
# print(delete_fruit)
# print(delete_fruit_last)
# print(fruits)

# Поиск элементов
# print(fruits.index("груша"))
# print(fruits.index("груш"))  # будет ошибка ValueError, так как такого элемента нет в списке
# print(fruits.count("банан"))
# fruits.remove("виноград")

# if "виноград" in fruits:
#     print("виноград найден")
# else:
#     print("не найден")

# Сортировка и реверс
# numbers = [1, 4, 6, 2, 9]
# new_numbers = sorted(numbers)  # не изменяет оригинальный список
# print(numbers)
# print(new_numbers)
# print(sorted(new_numbers, reverse=True))
# print(list(reversed(numbers)))  # не изменяет оригинальный список
# print(reversed(numbers))

# numbers.sort()  # изменяет оригинальный список
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# numbers.reverse()  # изменяет оригинальный список
# print(numbers)

# Минимум и максимум
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(min(fruits))
# print(max(fruits))

# Копирование списков
# new_numbers = numbers
# new_numbers = numbers.copy()
# print(id(numbers))
# print(id(new_numbers))
# new_list = new_numbers[:]
# print(new_numbers)
# print(new_list)

# Сумма элементов списка
# my_list_numbers = [1, 2, 3, 4, 5.99]
# print(sum(my_list_numbers))
# invalid_numbers = [1, 2, 3, "4", 5.99]
# print(sum([x for x in invalid_numbers if isinstance(x, int)]))

