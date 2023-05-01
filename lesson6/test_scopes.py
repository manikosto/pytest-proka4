import pytest
import time
import requests
import sqlite3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.mark.usefixtures("generate_login")
class TestLogin:

    @pytest.mark.scope
    def test_login_in_account(self):
        # self.driver.get("https://vk.com")
        print(self.login)

    @pytest.mark.scope
    def test_login_in_account_2(self):
        # self.driver.get("https://yandex.ru/login")
        print(self.login)
