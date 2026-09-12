from lessons.lesson_19.tests.test_data.data_test import DataTest


class ProductAssertions:
    def base_assertions(self, response):
        assert response["success"] == True
        assert response["data"]["description"] == DataTest.description
        assert response["data"]["price"] == 1
        assert response["data"]["quantity"] == 2