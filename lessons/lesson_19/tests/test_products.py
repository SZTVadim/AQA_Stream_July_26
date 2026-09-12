import pytest

from lessons.lesson_19.tests.test_data.data_test import DataTest


class TestProducts:
    @pytest.mark.parametrize("name, description, price, quantity",
                             [("rulon", "oboev", 1, 1), ("rulon2", "oboev2", 2, 2), ("rulon3", "oboev3", 3, 3)],
                             ids=["case1", "case2", "case3"])
    def test_create_product(self, products, delete_product, products_helper, product_assertions, name, description,
                            price, quantity):
        response = products.create_product(name, description, price, quantity)
        res_json = response.json()
        products_helper.remember_product(response.json()["data"]["id"])
        assert response.status_code == 201
        # assert res_json["data"]["name"] == DataTest.name
        # product_assertions.base_assertions(res_json)

    def test_get_product(self, products, setup_teardown_product, product_assertions):
        response = products.get_product(setup_teardown_product)
        res_json = response.json()

        assert response.status_code == 200
        assert DataTest.name in res_json["data"]["name"]
        product_assertions.base_assertions(res_json)

    def test_delete_product(self, products, product_id, product_assertions):
        response = products.delete_product(product_id)
        res_json = response.json()
        assert DataTest.name in res_json["data"]["name"]
        product_assertions.base_assertions(res_json)
