import requests


class TestInsultPage:

    def test_generate_insult(self):
        response = requests.get("https://evilinsult.com/generate_insult.php")
        assert response.status_code == 200, "Запрос на получение оскорбления сломан"