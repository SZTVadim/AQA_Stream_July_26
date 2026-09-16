import requests


class BaseApi:
    BASE_URL = "https://practice-api-qa.herokuapp.com"

    def get(self, endpoint, headers=None, **kwargs):
        return requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, **kwargs)

    def post(self, endpoint, headers=None, json=None, **kwargs):
        return requests.post(f"{self.BASE_URL}/{endpoint}", json=json, headers=headers, **kwargs)

    def put(self, endpoint, json=None, headers=None, **kwargs):
        return requests.put(f"{self.BASE_URL}/{endpoint}", json=json, headers=headers, **kwargs)

    def delete(self, endpoint, headers=None, **kwargs):
        return requests.delete(f"{self.BASE_URL}/{endpoint}", headers=headers, **kwargs)

    # def my_request(self, method, endpoint, **kwargs):
    #     return requests.request(method=method, url=f"{self.BASE_URL}/{endpoint}", json=None, **kwargs)
