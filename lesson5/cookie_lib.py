import json

def save_logged_cookies(driver, cookie_name):
    cookie = driver.get_cookie(cookie_name)
    with open("cookies.json", "w") as file:
        json.dump(cookie, file)

def load_saved_cookie(driver):
    driver.delete_all_cookies()
    with open("cookies.json", "r") as file:
        cookie = json.load(file)
    print(cookie)
    driver.add_cookie(cookie)
    driver.refresh()