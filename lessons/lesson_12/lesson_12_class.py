# Классы
ages = 22  # переменная


def say_hello():  # функция
    print("Hello")


class Dog:
    age_1 = 22  # атрибут

    def __init__(self, name):
        self.name = name

    def sound():  # метод
        return print("Гав-гаа")


dog = Dog("Boss")
dog1 = Dog("Boss")
print(id(dog))
print(id(dog1))

print(dog.name)
dog.sound()


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self, age):
        print(f"я {self.name}, мне {age} года")


person1 = Person("John")
print(person1.name)
person1.greeting(22)

person2 = Person("Kate")
print(person2.name)
person2.greeting(33)
#
