import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestPages: # Название тестового класса

    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    @pytest.mark.parametrize(
        "domain", [
            "https://demoqa.com/login", # URL для первого теста
            "https://demoqa.com/books", # URL для второго теста
            "https://demoqa.com/profile" # URL для третьего теста
        ]
    )
    def test_open_pages(self, domain):
        self.driver.get(domain)
        assert self.driver.current_url == domain, "Страница не была открыта"

    @pytest.mark.skip(reason="In progress...")
    def test_signup(self):
        self.driver.find_elements()

    def teardown(self):
        self.driver.close()