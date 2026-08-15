

def validate_age(age):
    if age >= 18:
        print("Доступ разрешен")
    else:
        print("Доступ запрещен")

# validate_age(17)
# validate_age(19)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list_new = []
for i in my_list:
    if i > 5:
        my_list_new.append(i)
# print(my_list_new)

# if–elif–else
score = 73
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
# print(grade)

# Вложенные условия
# number = 1
# if number >= 0:
#     if number < 10:
#         print(f"{number} является цифрой")
#     else:
#         print(f"{number} является числом")

# Пример использования условных конструкций
def check_temp(t):
    if t < 0:
        return "Мороз"
    elif t < 20:
        return "Прохладно"
    elif t < 30:
        return "Тепло"
    else:
        return "Жарко"

# print(check_temp(18))
a = 1
# match / case
def engine(comand):
    match comand:
        case "start":
            return "Запуск двигателя"
        case "stop":
            return "Двигатель заглушен"
        case _:
            return "Неизвестная команда"



print(engine("start"))
print(engine("stop"))


def check_status(status):
    match status:
        case 200:
            print("OK")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case _:
            print("Other")
