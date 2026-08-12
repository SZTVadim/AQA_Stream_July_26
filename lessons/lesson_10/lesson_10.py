data = [1, 2, 3]
# a, b, c = data
# a, b, c = [1, 2, 3]
# print(a)
# print(b)
# print(c)

coordinates = (10, 20)
# x = coordinates[0]
# y = coordinates[1]
x, y = coordinates
# print(x)
# print(y)

e, r = "hi"
# print(e)
# print(r)

first, *second = data
# print(first, second)

numbers = [1, 2, 3, 4, 5]
a, *middlle, b = numbers
# print(a)
# print(middlle)
# print(b)

my_set = {"apple", "banana", "cherry"}
apple, banana, cherry = my_set
# print(apple)
# print(banana)
# print(cherry)

# Распаковка словаря
student = {"name": "Иван", "возраст": 20, "город": "Москва"}
# for key, value in student.items():
    # print(key, value)

student_1 = {"name": "Иван", "size_jacket": "54", "age": 20, "city": "Tver"}
student_1.pop("city")

def my_func(name, age, size_jacket):
    print(f"{name} is {age} years old, and size: {size_jacket}")

# my_func("Vasya", 30, 54)
# my_func(**student_1)
# my_func(**student_1)

my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]
merge_list = [*my_list_1, *my_list_2]
# print(merge_list)

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 4, "e": 5}
merge_dict = {**dict_1, **dict_2}
merge_list1 = dict_1 | dict_2
# print(merge_dict)


# *args и **kwargs
def summ_data(aa, bb, gg):
    return print(aa + bb + gg)

# summ_data(1, 2, 3)
tuple1 = (1, 2, 3)

# summ_data(*tuple1)
# summ_data(1, 2, 3)

def summ_any_args(*args):
    print(sum(*args))

# summ_any_args(range(1, 1000000))

# Позиционые аргументы
def args_func(one: int, two: str, three):
    print(f"one это {one}, two это {two}, three это {three}")

one = 1
two = "2"
three = 3.33
# args_func(one, two, three)

# Именованные аргументы
# args_func(one=100, two="Двести", three=True)

def process_data(*args, **kwargs):
    print("Позиционные аргументы:", args)
    print("Именованные аргументы:", kwargs)
    print(f"Всего позиционных: {len(args)}")
    print(f"Всего именованных: {len(kwargs)}")

process_data("banana", True, 3.44, 10, [], {"a":1}, name="Ivan", age=20, city="Tver", my_bool=False)


text ="""Автоматизация тестирования — это практика, при которой проверки программного обеспечения выполняются с помощью
 специальных скриптов и инструментов, а не только вручную. Ручное тестирование остаётся важным: оно помогает 
 находить неочевидные дефекты, оценивать удобство интерфейса и проверять сложные пользовательские сценарии. 
 Однако когда продукт растёт, количество регрессионных проверок увеличивается, и повторять одни и те же шаги
  каждый день становится дорого и утомительно.
  
  Test automation is the practice of verifying software behavior with scripts and tools instead of relying only 
  on manual checks. Manual testing remains valuable: it helps discover unexpected defects, evaluate usability,
  and explore complex user journeys. However, as a product grows, the number of regression checks increases, and 
  repeating the same steps every day becomes expensive and exhausting.
  """