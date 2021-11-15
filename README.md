# AQA_BaseCamp_2021
pytest.ini --> help to change behavior of the tests by default

instead of:

    #     assert CreateUserRequests().create_users()[1] == OK_STATUS_SODE, "Code doesn't match"
    #     assert CreateUserRequests().get_user()[1] == OK_STATUS_SODE, "Code doesn't match"
    #     assert CreateUserRequests().put_user()[1] == OK_STATUS_SODE, "Code doesn't match"
    #     assert CreateUserRequests().delete_user()[1] == OK_STATUS_SODE, "Code doesn't match"
    #     assert CreateUserRequests().login_user()[1] == OK_STATUS_SODE, "Code doesn't match"
    #     assert CreateUserRequests().logout_user()[1] == OK_STATUS_SODE, "Code doesn't match"

I have used pytest.mark.parametrize in order to avoid duplicated code