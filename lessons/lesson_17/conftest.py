import pytest

from lessons.lesson_16.lesson_16 import Car


@pytest.fixture
def my_fixture():
    print("Создали клиента")
    car = Car("Toyta", "Corolla", 2000)
    yield car
    print("Удаляем нашего клиента после теста")
