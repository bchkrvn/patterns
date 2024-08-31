import requests.exceptions
from requests import Session


class SessionDecorator(requests.Session):
    def __init__(self, session: Session, tries_count: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__session = session
        self.__tries_count = tries_count

    def request(self, method, url, *args, **kwargs):
        for i in range(self.__tries_count):

            try:
                return self.__session.request(method, url, *args, **kwargs)
            except requests.exceptions.Timeout as ex:
                if i == self.__tries_count - 1:
                    raise ex
                else:
                    print('TIMEOUT')
                    continue
