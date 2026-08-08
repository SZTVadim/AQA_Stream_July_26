# Gerasimchuk_E
# Lesson 9 — индивидуальные задания

# ========== Часть 1 (задача 20) ==========
# Задача 20: Смешанная (str + int)
# Дана строка с числом:
value = "150"
# 1. Преобразуйте в int
# 2. Умножьте на 2
# 3. Преобразуйте результат обратно в str

value = int(value)
value = value * 2
value = str(value)
print(value)


# ========== Часть 2 (задача 11) ==========
# Задача 11:
# Дан URL:
url = "https://site.com/api/v1/users?id=15"
# Проверьте, что URL содержит "/api/",
# и извлеките query-параметр ключ и значение(записать все в отдельные пременные) id строковыми методами (без библиотек).

flag_api = "/api/" in url
url_dict = url.split("?")
key, value = url_dict[-1].split('=')
print(key)
print(value)