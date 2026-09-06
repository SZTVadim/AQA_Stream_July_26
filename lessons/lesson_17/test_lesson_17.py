import json
import math
import datetime

import pytest
import requests

# from datetime import datetime

# from lessons.lesson_14.lesson_14 import Car


# print(math.sqrt(16))
# print(datetime.datetime.now())

# def test_validate_data():
#     response = requests.get("https://practice-api-qa.herokuapp.com/api/products")
#     print(1)
#     assert response.status_code == 201, f"expected 201, received {response.status_code}"
#     print(2)
#     data = response.json()
#     assert data["success"] == True
#     assert isinstance(data["data"], list)
#     assert all(isinstance(i, dict) for i in data["data"])
#     print(data["data"])
#     f_el = data["data"][0]
#
#     assert isinstance(f_el["id"], int)
#
# def test_second():
#     response = requests.get("https://practice-api-qa.herokuapp.com/api/products")
#     assert response.status_code == 200
a = 1
def test_second_1(my_fixture):
    response = requests.get("https://practice-api-qa.herokuapp.com/api/products")
    assert response.status_code == 200
    print(my_fixture.brand)

@pytest.mark.parametrize("status_code", [200, 201, 404])
def test_status_code(status_code):
    response = requests.get("https://practice-api-qa.herokuapp.com/api/products")
    assert response.status_code == status_code
