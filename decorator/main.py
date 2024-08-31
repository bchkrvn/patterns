from requests import Session
from decorator.decorator_model import SessionDecorator

session = Session()
session_decorator = SessionDecorator(session, 5)

if __name__ == '__main__':
    url = 'https://example.com'
    response = session_decorator.get(url)
    print(response.status_code)
