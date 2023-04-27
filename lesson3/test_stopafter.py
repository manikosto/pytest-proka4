import time
import pytest

class TestStop:

    def test_1(self):
        assert 2 == 21, "Ошибка"
        time.sleep(2)

    def test_2(self):
        assert 2 == 1, "Ошибка"
        time.sleep(2)

    @pytest.mark.smoke
    def test_3(self):
        assert 2 == 2, "Ошибка"
        time.sleep(2)

    def test_4(self):
        assert 2 == 2, "Ошибка"
        time.sleep(2)

    def test_5(self):
        assert 2 == 2, "Ошибка"
        time.sleep(2)