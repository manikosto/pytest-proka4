import pytest
import time
import requests
import sqlite3
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(autouse=True)
def browser(request):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    request.cls.driver = driver
    yield # Ваш тест
    driver.quit()

@pytest.fixture(scope="function")
def generate_login(request):
    # Генерирует логин
    request.cls.login = f"autotest_{time.time()}@hyper.org"

@pytest.fixture
def generate_data(request):
    request.cls.login = f"autotest_{time.time()}@hyper.org"
    request.cls.password = "111"

@pytest.fixture
def get_insult(request):
    response = requests.get("https://evilinsult.com/generate_insult.php")
    request.cls.response = response


@pytest.fixture
def connect_database():

    # Установка соединения с базой данных
    connection = sqlite3.connect("/Users/manikosto/AquaProjects/PytestIntensive/lesson5/test.db")

    print("Соеденение с БД установлено")

    # Возвращение соеденения с БД
    return connection

# @pytest.fixture
# def generate_data():
#     login = f"autotest_{time.time()}@hyper.org"
#     password = "111"
#     return {"login": login, "password": password}



