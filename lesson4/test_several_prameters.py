


# class TestExample:
#
#     @pytest.mark.parametrize(
#         "login, password", [
#             ("manikosto", "qwerty123"),
#             ("HumUs12", "iuyatsdfK"),
#             ("Lion25R", "fasdgf234")
#         ]
#     )
#     def test_print_people(self, login, password):
#         print(login, password)

import pytest
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPages:

    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    @pytest.mark.parametrize(
        "domain, title", [
            ("https://demoqa.com/login", "DEMOQA"), # значения domain и title для первого теста
            ("https://wikipedia.org/", "Wikipedia"), # значения domain и title для второго теста
            ("https://yandex.ru", "Дзен") # значения domain и title для третьего теста
        ]
    )
    def test_open_pages(self, domain, title):
        self.driver.get(domain)
        assert self.driver.current_url == domain
        assert self.driver.title == title

    def teardown(self):
        self.driver.quit()