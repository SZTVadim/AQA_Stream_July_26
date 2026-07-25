# text = "Hello"
# print(id(text))
# text = "hello"
# print(id(text))
# number = 5
# number_1 = 5
# print(type(text))
# print(type(number))
# print(number + number_1)
# print(text + text)

# Строка
# text[0] = "h"  # Ошибка! Строки неизменяемые
# new_text = "h" + text[1:]
# print(new_text)

# Основные операции со строками - Преобразование регистра
# preobrazobvanie = "pyTHoN proGraMMing"
# lower_text = preobrazobvanie.lower()
# upper_text = preobrazobvanie.upper()
# capitalized_text = preobrazobvanie.capitalize()
# title_text = preobrazobvanie.title()
# print(lower_text)
# print(upper_text)
# print(capitalized_text)
# print(title_text)


# Основные операции со строками - Удаление(по дефолту пробелов)
# print("  test  ".strip())
# print(" test ".lstrip())
# print(" test ".rstrip())
# print(".50b% ".rstrip("b% ").lstrip("."))


# Основные операции со строками - Разделение и объединение строк
# text = "яблоко,банан,апельсин"
# print(text)
# list_from_str = text.split(",")
# print(list_from_str)
# text = ", ".join(list_from_str)
# print(text)
# print(type(text))

# Основные операции со строками - Замена подстрок
# text_ = "Я люб%лю Java%. Ja%va - э%то к%рут%о"
# new_text = text_.replace("Java", "Python")
# new_text = text_.replace("%", "")
# print(new_text)

# Основные операции со строками - Поиск и подсчет
# text_search = "Python программирование на Python"
# print(text_search.find("на"))
# print(text_search.find("java"))
# print(text_search.count("Python"))
# print(text_search.index("на"))
# print(text_search.index("наa"))  # Получим ошибку, так как ничего не найдено

# Основные операции со строками - Проверка типа символов
# print("hello".isalpha())
# print("hello1".isalpha())  # False т.к содержит еще и цифру
# print("123".isdigit())
# print("HELLO123".isalnum())
# print("HELLO123 ".isalnum())  # False т.к содержит еще пробел
# print("   ".isspace())

# Основные операции со строками - Преобразование между строками и числами
# a = "10.1"
# b = 20
# print(type(str(float(a) * b)))
# print(str(float(a) * b))

# Основные операции со строками - Срезы строк
# text_by_srez = "Инкапсуляция и полиморфизм"
# print(text_by_srez[7:])
# print(text_by_srez[:7])
# print(text_by_srez[:])
# print(text_by_srez[5:20])
# print(text_by_srez[5:20:3])

# Переворот текста
# reverse_text = text_by_srez[::-1]
# print(reverse_text)

# Основные операции со строками - Экранирование символов
# text_screen = "\tPython \n\"програмирование\""
# print(text_screen)

# Основные операции со строками - Тройные кавычки(многострочный комментарй)
# text = """Это
# "'многострочный'"
# текст"""
# print(text)