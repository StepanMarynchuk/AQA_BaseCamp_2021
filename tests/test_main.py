import pytest

import project
from project import *
import requests

OK_STATUS_SODE = 200


class TestApi():

    def test_get_status_code(self):
        assert sample_response.get()[1] == OK_STATUS_SODE, "Code doesn't match"

    def test_get_response(self):
        assert "true" in sample_response.get()[0]

    def test_post_status_code(self):
        assert sample_response.post()[1] == OK_STATUS_SODE, "Code doesn't match"

    def test_post_response(self):
        assert "505" in sample_response.post()[0]

    def test_put_status_code(self):
        assert sample_response.put()[1] == OK_STATUS_SODE, "Code doesn't match"

    def test_put_response(self):
        assert "postman-echo.com" in sample_response.put()[0]
