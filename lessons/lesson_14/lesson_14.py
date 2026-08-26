# Абстракция в ООП

from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        print("Двигатель заглушен")


class GasolineCar(Car):
    def start_engine(self):
        print("Громкий рев двигателя")


class ElectricCar(Car):
    def start_engine(self):
        print("Безшумный старт двигателя")


# car_g = GasolineCar()
# car_g.start_engine()
# car_g.stop_engine()
#
# car_e = ElectricCar()
# car_e.start_engine()
# car_e.stop_engine()


# Инкапсуляция в ООП
class Кофемашина:

    def нагреть_воду(self):
        print("Нагреваю воду...")

    def помолоть_зерна(self):
        print("Мелю зерна...")

    def сварить_кофе(self):
        print("Варю кофе...")

    def сделать_кофе(self):
        self.нагреть_воду()
        self.помолоть_зерна()
        self.сварить_кофе()
        return "Готовый кофе"

    def сделать_кофе_с_молоком(self):
        self.нагреть_воду()
        self.помолоть_зерна()
        self.сварить_кофе()
        print("Добавить молока")


# машина = Кофемашина()
# print(машина.сделать_кофе())  # Готовый кофе


class BankAccount:
    def __init__(self, initial_balance=0):
        # __balance - приватное поле (скрыто от прямого доступа)
        self.__balance = initial_balance

    # Публичные методы - интерфейс для взаимодействия
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение: +{amount} руб.")
        else:
            print("Сумма должна быть положительной")

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            print(f"Снятие: -{amount} руб.")
        else:
            print("Недостаточно средств или неверная сумма")

    def get_balance(self):
        return self.__balance


# Наследование

class OldCar:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class NewElectricCar(OldCar):
    def __init__(self, brand, model, battery_level):
        super().__init__(brand, model)
        self.battery_level = battery_level

    def display_info(self):
        print(f"Электромобиль: {self.brand} {self.model}, Заряд: {self.battery_level}%")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Батарея заряжена до {self.battery_level}%")


new_el_car = NewElectricCar("Tesla", "Model 3", battery_level=50)
new_el_car.display_info()
new_el_car.charge(1010)
new_el_car.display_info()


# Полиморфизм
class Собака:
    def звук(self):
        return "Гав-гав!"


class Кошка:
    def звук(self):
        return "Мяу!"


class Корова:
    def звук(self):
        return "Мууу!"


def издавать_звук(животное):
    return животное.звук()

собака = Собака()
кошка = Кошка()
корова = Корова()
print(собака.звук())


# издавать_звук(кошка)
# издавать_звук(корова)
print(издавать_звук(собака))



class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")


class Dog(Animal):
    def type_animal(self):
        return "Собака"

my_dog = Dog("Boss")
print(my_dog.type_animal())
my_dog.eat()

class BankAccountt:
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

