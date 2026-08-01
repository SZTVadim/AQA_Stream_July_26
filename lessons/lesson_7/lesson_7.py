# Кортежи

my_tuple = (1, 2, 3, 55, 55)
my_tuple_1 = 1, 2, 3
mixed_tuple = (1, "2", True)
# print(my_tuple)
# print(my_tuple_1)
# print(mixed_tuple)

# Кортежи из одного элемента
not_tuple = (5)
real_tuple = (5,)
real_tuple_1 = 5,

# print(type(not_tuple))
# print(type(real_tuple))
# print(type(real_tuple_1))

# Основыне операции с кортежами
# print(my_tuple[-1])
# print(my_tuple_1[1:3])
# print(3 in my_tuple)
# print(4 in my_tuple)
# print(len(my_tuple))

# поиск и подсчет
# print(my_tuple.index(55))
# print(my_tuple.count(55))

# объединение кортежей
tuple1 = (1, 2, 3)
tuple2 = (4, 5)

combined_tuple = tuple1 + tuple2
# print(combined_tuple)

repeated_tuple = tuple1 * 4
# print(repeated_tuple)

# Использование кортежа как ключа для словаря(dict)
coord_work = (135, 160)
coord_home = (10, 120)
coord  = {coord_work: "Работа", coord_home: "Дом"}
# print(coord[135, 160])
# print(coord[10, 120])

# print(hash(coord_work))
# print(hash(coord_home))
# print(hash([1, 2, 3])) # список не хешируемый, поэтому нельзя использовать как ключ в словаре

# Распаковка кортежей
# first = tuple1[0]
# second = tuple1[1]
# last = tuple1[-1]
# first, second, last = tuple1  # когда надо распаковать все значения каллекции по своим переменным
# first, *second = tuple1  # когда надо распаковать кортеж в переменные(при условии, что переменных меньше чем элементов коллекции)
first, *_, last = tuple1  # когда надо распаковать только первое и последнее значение корежа, а остальное выбросить

# print(first)
# print(second)
# print(last)

# Как поменять значение в кортеже
# list_from_my_tuple = list(my_tuple)
# print(list_from_my_tuple)
# list_from_my_tuple.append(555)
# print(list_from_my_tuple)
# new_my_tuple = tuple(list_from_my_tuple)
# print(new_my_tuple)

# Обмен значений переменных
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)
