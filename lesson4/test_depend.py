import pytest
import requests


class TestDependens:

    @pytest.mark.dependent
    @pytest.mark.dependency(name="Create task")
    def test_create_task(self):
        assert True

    @pytest.mark.dependent
    @pytest.mark.dependency(depends=["Create task"], name="Change description")
    def test_change_task_description(self):
        assert True

    @pytest.mark.dependent
    @pytest.mark.dependency(depends=["Create task"])
    def test_delete_task(self):
        assert True