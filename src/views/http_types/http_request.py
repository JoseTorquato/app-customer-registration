from typing import Dict


class HttpRequest:
    def __init__(self, header: Dict = None, body: Dict = None, url: str = None) -> None:
        self.header = header
        self.body = body
        self.url = url
