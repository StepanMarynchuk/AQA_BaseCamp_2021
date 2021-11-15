import pytest

from AQA_BaseCamp_2021.api_requests.project import *

OK_STATUS_CODE = 200


class TestApi():
    @pytest.mark.parametrize('code_method',
                             [('CreateUserRequests().create_users()[1]'), ('CreateUserRequests().get_user()[1]'),
                              ('CreateUserRequests().put_user()[1]'), ('CreateUserRequests().delete_user()[1]'),
                              ('CreateUserRequests().login_user()[1]'), ('CreateUserRequests().logout_user()[1]')])
    def test_status_code(self, code_method):
        assert eval(code_method) == OK_STATUS_CODE

    def test_create_user(self):
        assert CreateUserRequests().create_users()[0] == "ok", "User's can't be added"

    def test_update_user(self):
        assert CreateUserRequests().put_user()[0]["message"] == str(new_users_data["id"])

    def test_delete_usre(self):
        assert CreateUserRequests().delete_user()[0] == users_list[1]["username"]

    def test_login_user(self):
        assert "logged in" in CreateUserRequests().login_user()[0]["message"]

    def test_logout_user(self):
        assert CreateUserRequests().logout_user()[0]["message"] == "ok"
