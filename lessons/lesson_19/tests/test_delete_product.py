from lessons.lesson_19.tests.test_data.data_test import DataTest


class TestDeleteProduct:
    def test_delete_product(self, products, product_id, product_assertions):
        response = products.teardown_product(product_id, )
        res_json = response.json()
        assert DataTest.name in res_json["data"]["name"]
        product_assertions.base_assertions(res_json)

    def test_delete_product_not_found(self, products):
        response = products.delete_product(1)
        print(response.json())
        assert response.status_code == 404

    def test_delete_all(self, products):
        all_products = products.get_products().json()["data"]
        for p in all_products:
            products.delete_product(p["id"])



