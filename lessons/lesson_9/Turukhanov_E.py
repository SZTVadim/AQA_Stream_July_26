# Turukhanov_E
# Lesson 9 — индивидуальные задания

# ========== Часть 1 (задача 19) ==========
# Задача 19: Работа с bool
# Дан статус код и флаг:
status_code = 200
has_body = True
# Получите bool: успешен ли ответ?
# Условие: status_code == 200 и has_body == True
print(status_code == 200 and has_body == True)

# ========== Часть 2 (задача 5) ==========
# Задача 5:
# Получите новый список только валидных email (условие: содержит "@" и ".").
# Заменить последний элемент коллекци, исправив "," на "."
emails = ["a@test.com", "bad-email", "b@site,org"]
emails[-1] = emails[-1].replace(",",".")
new_email = [email for email in emails if "@" in email and "." in email]

print(new_email)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)