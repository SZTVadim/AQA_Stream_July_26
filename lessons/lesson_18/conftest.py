import pytest

from lessons.lesson_18.lesson_18 import delete_pet, get_pet, create_pet


@pytest.fixture
def teardown_pet():
    id_pets = []
    yield id_pets
    for p in id_pets:
        delete_pet(p)

@pytest.fixture
def id_pet():
    id_pet = create_pet().json()["id"]
    yield id_pet

@pytest.fixture
def setup_teardown(id_pet, teardown_pet):
    teardown_pet.append(id_pet)
    yield id_pet


