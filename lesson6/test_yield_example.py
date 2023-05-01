import pytest
import time
import requests
import sqlite3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestLogin:

    @pytest.mark.login
    def test_login_in_account(self):
        self.driver.get("https://www.freeconferencecall.com/login")
        print("HELLO 1")

    @pytest.mark.login
    def test_login_in_account_2(self):
        self.driver.get("https://www.yandex.ru")
        print("HELLO 2")