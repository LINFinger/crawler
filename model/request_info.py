from constant import request


class RequestInfo:
    def __init__(self):
        self.headers = request.BACKUP_HEADERS
        self.cookies = request.BACKUP_COOKIES

    @classmethod
    def headers_only(cls, headers):
        cls.headers = headers
        cls.cookies = request.BACKUP_COOKIES
        return cls

    @classmethod
    def all(cls, headers, cookies):
        cls.headers = headers
        cls.cookies = cookies
        return cls
