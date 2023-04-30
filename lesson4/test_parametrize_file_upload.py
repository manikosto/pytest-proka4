import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPages:

    def setup(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    @pytest.mark.parametrize(
        "path_to_file",
        [
            (f"{os.getcwd()}/uploads/document.doc"),
            (f"{os.getcwd()}/uploads/image.jpg"),
            (f"{os.getcwd()}/uploads/music.mp3"),
        ]
    )
    def test_file_upload(self, path_to_file):
        self.driver.get("https://demoqa.com/upload-download")
        self.driver.find_element("xpath", "//input[@type='file']").send_keys(path_to_file)
        time.sleep(2)

    def teardown(self):
        self.driver.quit()