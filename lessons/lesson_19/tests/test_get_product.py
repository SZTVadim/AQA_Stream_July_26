from lessons.lesson_19.tests.test_data.data_test import DataTest


class TestGetProduct:
    def test_get_product(self, products, setup_teardown_product, product_assertions):
        response = products.get_product(setup_teardown_product)
        res_json = response.json()
        print(len(res_json["data"]))
        # assert response.status_code == 200
        # assert DataTest.name in res_json["data"]["name"]
        # product_assertions.base_assertions(res_json)

    def test_len_p(self, products):
        res = products.get_products().json()
        print(len(res["data"]))