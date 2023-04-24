from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage: # Название тестового класса

    def test_open_login_page(self): # Название нашего теста
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.freeconferencecall.com/login")
        assert driver.title == "Log in page | FreeConferenceCall.com", "Страница логина не была открыта"
