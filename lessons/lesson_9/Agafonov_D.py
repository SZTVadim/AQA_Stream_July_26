# Agafonov_D
# Lesson 9 — индивидуальные задания

# ========== Часть 1 (задача 13) ==========
# Задача 13: Работа со строкой
# Дан email:
# email = "Test.User@Example.COM"
# 1. Приведите email к нижнему регистру
# 2. Разделите на имя и домен по "@"
# 3. Выведите имя и домен отдельно

# 1. Приведите email к нижнему регистру
# email = email.lower()
# 2. Разделите на имя и домен по "@"
# name, email = email.split("@")

# 3. Выведите имя и домен отдельно
# print(name)
# print(email)



# ========== Часть 2 (задача 7) ==========
# Задача 7:
# Создайте словарь только с endpoint, где код 200.
# В созданном словаре поменять значение login на 201.
pairs = [("login", 200), ("profile", 404), ("orders", 200)]

new_pairs = {endpoint: code for endpoint, code in pairs if code == 200}
new_pairs["login"] = 201
# print(new_pairs)


# Python 
# Нужно написать код для чисел от 1 до 100. Если число делится на 3, выводят «Fizz». Если делится на 5, выводят «Buzz». Если делится на 3 и на 5 сразу, выводят «FizzBuzz». В остальных случаях выводят само число.
# .



for number in range(1,101):
     if number % 3 == 0:
         print("Fizz")
     elif number % 5 == 0:
          print("Buzz")
     elif number % 3 == 0 and number % 5 == 0:
        print ("FizzBuzz")
     else:
        print(number)