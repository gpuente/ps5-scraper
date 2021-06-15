import asyncio
import requests
from aiohttp import ClientSession
from bs4 import BeautifulSoup

class SimpleScraper:
    NOT_EMPTY = 'not_empty'

    def __init__(self, url, selector, test, session: ClientSession, method="GET"):
        self.url = url
        self.test = test
        self.method = method
        self.session = session
        self.selector = selector
        self.__assert_prefix = "test_"

    async def get_soup(self):
        res = await self.session.request(method=self.method, url=self.url)
        res.raise_for_status()
        body = await res.text()

        return BeautifulSoup(body, "html.parser")

    def test_not_empty(self, soup: BeautifulSoup):
        element = soup.select_one(self.selector)
        return element != None

    def test_not_error_res():
        return True

    async def run_test(self, test_key=None):
        key = self.test if not test_key else test_key
        test_func = getattr(self, self.__assert_prefix + key)

        try:
            return test_func(await self.get_soup())
        except Exception as error:
            return False


