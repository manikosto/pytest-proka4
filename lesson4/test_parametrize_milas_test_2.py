import requests
import pytest


class TestPages:

    @pytest.mark.parametrize("domain", open("domains.txt").readlines())
    def test_open_pages(self, domain):
        url = domain.strip()
        response = requests.get(url)
        assert response.status_code == 200, "Страница не доступна"