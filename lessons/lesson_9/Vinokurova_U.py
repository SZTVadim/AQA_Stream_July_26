# Vinokurova_U
# Lesson 9 — индивидуальные задания

# ========== Часть 1 (задача 21) ==========
# Задача 21: Смешанная (str + float + bool)
# Дан текст:
message = "error: timeout after 2.5 sec"
# 1. Проверьте, что в тексте есть слово "error" (bool)

print("error" in message)

# 2. Извлеките число 2.5 из строки и преобразуйте в float
# вариант решения 1

print(message.find("2.5"))
dva = float(message[21:24])

print(type(dva))

# вариант решения 2

list = message.split()
dva_1 = float(list[3])

print(f'{dva_1} : {type(dva_1)}')

# ========== Часть 2 (задача 8) ==========
# Задача 8:
# Дан список URL с дублями. Получите количество уникальных URL.

urls = ["/login", "/login", "/profile", "/orders", "/orders"]

print(len(set(urls)))

# ПОменять последний индекс "/login" на "/logout"

urls.pop(1)
urls.insert(1, "/logout")
print(urls)

"""Python 
Нужно написать код для чисел от 1 до 100. 
Если число делится на 3, выводят «Fizz». 
Если делится на 5, выводят «Buzz». 
Если делится на 3 и на 5 сразу, выводят «FizzBuzz». 
В остальных случаях выводят само число.
"""
result = []

for i in range(1, 101):
    if i % 15 == 0:
        result.append("FizzBuzz")
    elif i % 5 == 0:
        result.append("Buzz")
    elif i % 3 == 0:
        result.append("Fizz")
    else: 
        result.append(i)
print(result)      
