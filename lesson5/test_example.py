import pytest

@pytest.mark.usefixtures("generate_data")
# @pytest.mark.usefixtures("browser")
class TestExample:

    # def test_example_1(self, generate_data):
    #     login = generate_data[0]
    #     password = generate_data[1]
    #     print(login, password)
    #
    # def test_example_2(self, generate_data):
    #     print(generate_data["login"])
    #     print(generate_data["password"])

    @pytest.mark.usefixtures("get_insult")
    def test_check_insult(self):
        print(self.response.status_code)

    def test_example_via_request(self):
        self.driver.get("https://yandex.ru")
        print(self.login)
        print(self.password)

    def test_example_via_request2(self):
        self.driver.get("https://vk.com")
        print(self.login)
        print(self.password)

    def test_example_via_request3(self):
        self.driver.get("https://google.com")
        print(self.login)
        print(self.password)

    def test_check_connection_to_db(self,  connect_database):
        cursor = connect_database.cursor()
        cursor.execute("SELECT * FROM employees")
        print(cursor.fetchall())
        connect_database.close()

