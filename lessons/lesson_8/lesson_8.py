# Генераторы списков (List Comprehensions)

numbers = [1, 2, 3, 4, 5.99]
# Способ через for
squares = []
# for i in numbers:
#     print(f"текущий элемент коллекции: {i}")
#     squares.append(i ** 3)
#     print(f"актуальное состояние коллекции {squares}\n")
# print(squares)

# Способ через генератор
# squares = [n ** 3 for n in numbers]
# print(squares)

# list_1 = [n for n in range(1, 334, 2)]
# print(list_1)

# words = ["helLLo", "WORLDD", "Apple"]
# lower_words = [x.lower() for x in words]
# print(lower_words)

# list_numbers = [x for x in range(10) if x % 2 == 0]
# print(list_numbers)

# words = ["cat", "dog", "elephant", "ant", "tiger"]
# long_words = [w for w in words if len(w) > 3]
# print(long_words)
#
# list_numbers_1 = [x ** 2 for x in range(10) if x % 2 == 0]
# print(list_numbers_1)

result = [x if x > 0 else f"элемент {x} не подходит" for x in range(-9, 10, 3)]
# print(result)


# Генераторы словарей (Dictionary Comprehensions)
# Создание словаря из списка:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares_dict = {f"element_{x}": x** 2 for x in numbers}
squares_dict = {f"element_{x}": x** 2 for x in range(1, 10)}
# print(squares_dict)

# Фильтрация элементов:
# even_squares = {f"element_{x}": x** 2 for x in numbers if x % 2 == 0}
# print(even_squares)

# Преобразование строкового ключа:
# words = ["apple", "banana", "lime"]
# length_dict = {w: len(w) for w in words}
# print(length_dict)


# Генераторы кортежей (Tuple Comprehensions)
gen = (x for x in range(1, 10))  # Это генератор, а не кортеж!
print(gen)
gen_1 = tuple(x for x in range(1, 10))
print(gen_1)

# Генераторы множества
set_gen = {x for x in range(1, 10) if x % 2 == 0}
print(set_gen)

