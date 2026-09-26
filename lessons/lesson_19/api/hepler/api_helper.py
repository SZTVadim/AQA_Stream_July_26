class ApiHepler:
    def __init__(self, token):
        self.token = token

    def _header(self, need_token=False):
        if need_token:
            return {
                    "Accept": "application/json",
                    "Authorization": f"Bearer {self.token}"}
        else:
            return {"Accept": "application/json"}
