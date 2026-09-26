from requests import Response


class Person:
    def получение_токена(selfб, емаил, пасс)-> Response:
        # отправить запрос и передать емаил и пасс
        # ВЕРНУТЬ CЫРОЙ ОТВЕТ
        pass

    def get_token(self):
        token =  self.получение_токена().json()
        return f"Bearer {token["token"]}"

    def регистрация_клиента(self):
        # отправить запрос и передать емаил и пасс и username
        # ВЕРНУТЬ ВЫРОЙ ОТВЕТ
        pass