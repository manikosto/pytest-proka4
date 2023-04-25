import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestExample:

    def setup(self): # Пред-условие
        print("Данный код выполняется до теста")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_broken(self):
        self.driver.get("https://ya.ru/")
        # pytest.set_trace() # Брейкпоинт пайтеста
        assert self.driver.title == "Hello", "Ошибка"
        assert 2 == 2, "Ошибка"

    def test_find_smth_in_yandex(self):
        # pytest.set_trace()
        self.driver.get("https://ya.ru/")
        search_field = self.driver.find_element("xpath", "//input[@id='text']")
        search_field.send_keys("Как играть на нервах")
        assert search_field.get_attribute("value") != "", "Запрос на поиск не введен"





    def teardown(self):
        print("Данный код выполняется после теста")