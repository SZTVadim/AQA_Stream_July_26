list_my = [1, 51, 45, -123, 5]
# print(list_my[-1])

student_one = {
    "имя": "Иван",
    "возраст": 20,
    "курс": 2
}
# print(student_one["имя"])
# print(student_one["курс"])
# student_one["курс"] = 3
# print(student_one)

person_second = {
    "name": "Ivan",
    "age": 21,
    "is_teacher": False,
    "is_student": True,
    "address": [{
        "city": "Saratov",
        "country": "Russia"
    },
        {"city": "SPB",
        "country": "Russia"}]
    }
# print(person_second["address"][1]["city"])

# Словари можно перебирать с помощью циклов for.

# my_dict = {"a": 1, "b": 2, "c": 3}
# for key in my_dict.items():  # получить пары (ключ, значение)
# for key in my_dict.keys():  # получить только ключи
# for key in my_dict.values():  # получить значения
#     print(key)

# prices = {"яблоко": 50, "банан": 30, "апельсин": 40}
# for fruit, price in prices.items():
#     if fruit == "банан":
#         price = price * 1.15
#     print(fruit, price)
# print(prices)


# Удаление элементов
# student_new = {"имя": "Иван", "возраст": 20, "курс": 2}

# age = student_new.pop("возраст")
# print(age)
# print(student_new)

# del student_new["курс"]
# print(student_new)

# student_new["is_student"] = True
# print(student_new)

# student_new.clear()
# print(student_new)

# Объединение словарей
dict_one = {"a": 1, "b": 2}
dict_two = {"c": 3, "d": 4}

dict_one.update(dict_two)
print(dict_one)

# Объединение нескольких словарей
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
dict1.update({"e": 5, "f": 6})
print(dict1)

# Слияние с одинаковыми ключами
dict1 = {"name": "Иван", "age": 25}
dict2 = {"age": 30, "city": "Москва"}
dict1.update(dict2)
print(dict1)