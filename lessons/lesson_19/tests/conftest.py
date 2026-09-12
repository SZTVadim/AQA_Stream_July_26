import time
import uuid

import pytest

from lessons.lesson_19.api.products import Products
from lessons.lesson_19.products_hepler.product_assertions import ProductAssertions
from lessons.lesson_19.products_hepler.products_helper import ProductsHelper
from lessons.lesson_19.tests.test_data.data_test import DataTest


@pytest.fixture()
def products():
    return Products()

@pytest.fixture()
def products_helper():
    return ProductsHelper()

@pytest.fixture()
def product_assertions():
    return ProductAssertions()

@pytest.fixture()
def new_product(products):
    # Setup new product
    now = time.time()
    response = products.create_product(uuid.uuid4().hex, DataTest.description, 1, 2)

    return response

@pytest.fixture()
def product_id(new_product):
    return new_product.json()["data"]["id"]

@pytest.fixture()
def delete_product(products, products_helper):
    yield
    products.delete_product(products_helper.product_id)

@pytest.fixture()
def setup_teardown_product(product_id, delete_product):
    yield product_id