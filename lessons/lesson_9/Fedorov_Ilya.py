# Fedorov_Ilya
# Lesson 9 — индивидуальные задания

# ========== Часть 1 (задача 17) ==========
# Задача 17: Работа с float
# Дано время ответа API:
# response_time = 0.3575
# 1. Переведите в миллисекунды (* 1000)
# 2. Округлите до целого
# 3. Проверьте, что результат < 500

# ========== Часть 2 (задача 6) ==========
# Задача 6:
# Получите список имен пользователей старше 18.
# users = [{"name": "Ann", "age": 20}, {"name": "Bob", "age": 17}, {"name": "Kate", "age": 25}]
# подменим возраст Боба на 19

response_time = 0.357
response_time_ms = response_time * 1000
response_time_ms = int(response_time_ms)
print(response_time_ms)
print(response_time_ms < 500)

users = [
    {"name": "Ann", "age": 20},
    {"name": "Bob", "age": 17},
    {"name": "Kate", "age": 25}]
names = [user["name"] for user in users if user["age"] > 18]
print(names)
users[1]["age"] = 19
print(users)
