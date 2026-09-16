import pytest

from lessons.lesson_19.tests.test_data.data_test import DataTest
from lessons.lesson_19.tests.test_data.type_response import TypeResponse


class TestCreateProduct:
    # @pytest.mark.parametrize("name, description, price, quantity",
    #                          [("rulon", "oboev", 1, 1), ("rulon2", "oboev2", 2, 2), ("rulon3", "oboev3", 3, 3)],
    #                          ids=["case1", "case2", "case3"])
    # def test_create_product(self, products, teardown_product, products_helper, product_assertions, name, description,
    #                         price, quantity):
    def test_create_product(self, products, teardown_product, products_helper, product_assertions):
        # response = products.create_product(name, description, price, quantity)
        response = products.create_product()
        res_json = response.json()
        products_helper.remember_product(response.json()["data"]["id"])
        assert response.status_code == 201
        assert res_json["data"]["name"] == DataTest.name
        product_assertions.base_assertions(res_json)

    @pytest.mark.parametrize("payload, name_test", [({"description": "oboev", "price": 1, "quantity": 1}, "имя"),
                                                    ({"name": "rulon", "price": 1, "quantity": 1}, "описание")],
                             ids=["no_name", "no_description"])
    def test_create_product_empty_data(self, products, teardown_product, payload, name_test):
        response = products.create_product(**payload)
        res_json = response.json()
        print(res_json)
        assert response.status_code == 400

        assert res_json["success"] == False
        assert res_json["error"] == f"[Поле {name_test} не может быть пустым]"

    def test_create_product_not_found(self, products, teardown_product):
        response = products.create_product(endpoint="api/my_endpoint")
        res_json = response.json()
        print(response)
        print(response.json())
