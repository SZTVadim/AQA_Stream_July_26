# Stygar_A
# Lesson 9 — индивидуальные задания

# ========== Часть 1 (задача 14) ==========
# Задача 14: Работа с числами (int)
# Даны два числа:
a = 17
b = 5
# Найдите:
# 1. сумму
# 2. частное (обычное деление)
# 3. целую часть от деления
# 4. остаток от деления

# ========== Часть 2 (задача 3) ==========
# Задача 3:
products = [{"id": 1, "name": "Phone"}, {"id": 2, "name": "Laptop"}]
# Извлеките name второго продукта (Laptop)
# Заменить id второго продукта на 3

# Задача 14: Работа с числами (int)
numbers = [17, 5]
print(sum(numbers))

result = a/b
print(result)

print(round(a/b))

print(a%b)

# Задача 3:
print(products[1]["name"])

products[-1]["id"]=3
print(products)

for numbers in range(1,101):

    if numbers % 15 == 0:
        print("FizzBuZZ")
    elif numbers % 3 == 0:
        print("Fizz")
    elif numbers % 5 == 0:
        print("Buzz")
    else:
        print(numbers)
        









