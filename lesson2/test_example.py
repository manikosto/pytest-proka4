import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestExample:

    def setup(self): # Пред-условие
        print("Данный код выполняется до теста")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_1(self):
        self.driver.get("https://ya.ru/")
        print("Тест 1...")

    def test_2(self):
        self.driver.get("https://facebook.com/")
        print("Тест 2...")

    def teardown(self):
        print("Данный код выполняется после теста")