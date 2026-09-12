import uuid


class ProductsHelper:
    product_id = None
    name = None
    description = None


    def remember_product(self, product_id):
        self.product_id = product_id

    def _name(self, name):
        self.name = name
print(uuid.uuid4().hex)