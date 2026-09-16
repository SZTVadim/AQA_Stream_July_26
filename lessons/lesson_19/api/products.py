from lessons.lesson_19.api.base_api import BaseApi


class Products(BaseApi):
    ENDPOINT = "api/products"
    HEADERS = {"accept": "*/*"}

    def create_product(self, name=None, description=None, price=None, quantity=None, endpoint=None):

        json = {"name": name, "description": description, "price": price, "quantity": quantity}
        if endpoint:
            return self.post(endpoint=endpoint, headers=self.HEADERS, json=json)
        return self.post(endpoint=self.ENDPOINT, headers=self.HEADERS, json=json)

    def get_product(self, product_id):
        return self.get(f"{self.ENDPOINT}/{product_id}")

    def get_products(self):
        return self.get(self.ENDPOINT)

    def delete_product(self, product_id):
        return self.delete(f"{self.ENDPOINT}/{product_id}")

    # TODO: "Бага в обьязательными полями"
    def update_product(self, product_id, name=None, description=None, price=None, quantity=None):
        json = {"name": name, "description": description, "price": price, "quantity": quantity}
        if not name:
            json.pop("name")
        if not description:
            json.pop("description")
        if not price:
            json.pop("price")
        if not quantity:
            json.pop("quantity")
        return self.put(f"{self.ENDPOINT}/{product_id}", json=json)
