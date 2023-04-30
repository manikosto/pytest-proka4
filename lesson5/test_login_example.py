import json
import time
import pytest
import os
from cookie_lib import *


@pytest.mark.usefixtures("browser")
class TestLogin:

    # def setup(self):
    #     self.driver.get("https://www.freeconferencecall.com/login")

    def test_login_in_account(self):
        self.driver.get("https://www.freeconferencecall.com/login")
        time.sleep(40)
        save_logged_cookies(self.driver, "_freeconferencecall_session")

    def test_change_profile_photo(self):
        self.driver.get("https://www.freeconferencecall.com/login")
        load_saved_cookie(self.driver)
        time.sleep(10)

