import requests.exceptions
from requests import Response


class FakeSession:
    def __init__(self):
        self.error_count = 3
        self.request_count = 0

    def request(self, *args, **kwargs):
        if self.request_count < self.error_count:
            self.request_count += 1
            raise requests.exceptions.Timeout()
        else:
            return Response()
