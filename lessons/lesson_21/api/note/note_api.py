from lessons.lesson_19.api.base_api import BaseApi


class NoteApi(BaseApi):
    def get_notes(self, token ,need_header=False):
        if need_header:
            res = self.get(endpoint='/api/notes', headers={"accept": "application/json", "Authorization":token})
            return res
        else:
            res = self.get(endpoint='/api/notes', headers={"accept": "application/json"})
            return res