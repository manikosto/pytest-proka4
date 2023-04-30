import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPages:

    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=self.service, options=options)

    @pytest.mark.parametrize("domain", open("domains.txt").readlines())
    def test_open_pages(self, domain):
        url = domain.strip()
        self.driver.get(url)
        assert self.driver.current_url in url, "Ошибка"

    def teardown(self):
        self.driver.quit()