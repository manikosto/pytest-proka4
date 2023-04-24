import requests

# assert <условие>, <кастомное сообщение об ошибке>

assert 2 == 2, "Ошибка"

assert "Hello" in "I love you, world"

response = requests.get("https://evilinsult.com/generate_insult.php")
assert response.status_code == 200, "Запрос на получение оскорбления сломан"
print(response.text)