# Менеджер контекста
# with open("test_lesson_16.txt", "w") as file:
#     file.write("Мы открыли файл и что-то туда записали")
from dataclasses import dataclass


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def service_check(self):
        # Метод имитирует проверку автомобиля в сервисе
        print(f"Проводится диагностика автомобиля {self.brand} {self.model}.")

    def __str__(self):
        return f"{self.brand} {self.model}"

class CarService:
    def __init__(self, car: Car):
        self.car = car

    def __enter__(self):
        # Код, выполняющийся при входе в контекст
        print(f"Автомобиль {self.car} поступил в сервисное обслуживание.")
        # Например, можно открыть соединение с оборудованием диагностики
        return self.car  # возвращаем автомобиль для работы внутри блока with

    def __exit__(self, exc_type, exc_value, traceback):
        # Код, выполняющийся при выходе из контекста
        if exc_type:
            print(f"Во время обслуживания автомобиля {self.car} произошла ошибка: {exc_value}")
        print(f"Автомобиль {self.car} покидает сервисное обслуживание.")
        # Здесь можно закрыть соединения, освободить ресурсы и т.д.
        # Возвращаем False, чтобы исключения, если они есть, не подавлялись.
        return False

# car = Car("Toyota", "Camry")
# print(car)
# print(str(car))

# С with
# with CarService(car) as service:
#     print("Работаем,,,")
#     raise ValueError("Error!")

# Это эквивалентно:
# service = CarService(car)
# try:
#     service.__enter__()
#     print("Работаем,,,")
# finally:
#     service.__exit__(None, None, None)


# dataclass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age

@dataclass
class PersonData:
    name: str
    age: int

person1 = Person("Иван", 25)
person3 = Person("Иван", 25)

person2 = PersonData("Мария", 30)

# print(person1)
# print(person2)
# print(person1 == person3)

# Итератор

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarLot:
    def __init__(self, cars):
        self.cars = cars
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.cars):
            car = self.cars[self.index]
            self.index += 1
            return car
        else:
            raise StopIteration


# Использование итератора:
lot = CarLot([
    Car("Toyota", "Corolla", 2020),
    Car("Honda", "Civic", 2019),
    Car("Ford", "Mustang", 2021)
])

# for car in lot:
#     print(car)

a = 1
# Генератор
def car_factory(total):
    """Генератор, имитирующий производство автомобилей."""
    for i in range(1, total + 1):
        yield Car("BrandX", f"Model-{i}", 2020 + i)

# for car in car_factory(5):
#     print(car)

factory = car_factory(6)

print(next(factory))
print(next(factory))
print(next(factory))
print(next(factory))
print(next(factory))




print("=" * 80)


print(next(factory))