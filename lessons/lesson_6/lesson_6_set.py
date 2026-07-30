# Множества - коллекции уникальных элементов

# numbers ={1, 2, 2, 3, 3, 4, 5 ,5}
# print(numbers)

numbers = {1, 22, 333, 341, 434, 4, 5}
# print(numbers)

fruits = {"apple", "banana", "cherry", "mango"}
# print(fruits)

list_numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# print(list(set(list_numbers)))
# print(list_numbers)


# добавления элементов во множество
fruits_my = {"apple", "banana"}
fruits_my.add("mango")
# print(fruits_my)
fruits_my.update(["груша", "виноград"])
print(fruits_my)

# Удаление элементов

fruits_my.discard("mango")
print(fruits_my)
fruits_my.discard("mango")
print(fruits_my)

# fruits_my.remove("mango")  # Ошибка KyeError
fruits_my.remove("apple")
print(fruits_my)
removed_fruit = fruits_my.pop()
print(removed_fruit)
print(fruits_my)
