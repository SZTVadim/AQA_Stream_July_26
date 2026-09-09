import pytest

from lessons.lesson_18.lesson_18 import create_pet, get_pet, delete_pet, put_pet


def test_create_pet(teardown_pet):
    response = create_pet()
    id_pet = response.json()["id"]
    assert response.status_code == 200, f"Ожидали статус код 200, получили: {response.status_code}"
    assert "id" in response.json()
    assert isinstance(response.json()["id"], int)
    teardown_pet.append(id_pet)


def test_get_pet(setup_teardown):
    response = get_pet(setup_teardown)

    assert response.status_code == 200
    assert "id" in response.json()
    assert isinstance(response.json()["id"], int)

@pytest.mark.smoke
def test_put_pet(setup_teardown):
    response = put_pet(setup_teardown)
    response_json = response.json()
    assert response.status_code == 200, f"expect: 200, actual: {response.status_code}"
    assert response_json["category"]["id"] == 6
    assert response_json["category"][
               "name"] == "Kot", f"Ожидали получить 'Kot', получили {response_json['category']['name']}"
    assert response_json["name"] == "Barsik"

@pytest.mark.regression
def test_delete_pet(id_pet):
    response = delete_pet(id_pet)
    response_json = response.json()
    assert response.status_code == 200, f"expect: 200, actual: {response.status_code}"
    assert response_json["type"] == "unknown"
    assert response_json["message"] == str(id_pet)

    response_get = get_pet(id_pet)
    assert response_get.status_code == 404
