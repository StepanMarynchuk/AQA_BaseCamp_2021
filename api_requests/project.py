import requests

from AQA_BaseCamp_2021.requests.data import *


class CreateUserRequests():

    def create_users(self):
        post_response = requests.request("POST", base_url + create_users_endpoint, headers=headers, data=payload)
        return post_response.json()["message"], post_response.status_code

    def get_user(self):
        get_response = requests.request("GET", base_url + users_list[1]["username"], headers=headers, data=payload)
        return get_response.json(), get_response.status_code

    def put_user(self):
        put_response = requests.request("PUT", base_url + users_list[0]["username"], headers=headers,
                                        data=payload_update)
        return put_response.json(), put_response.status_code

    def delete_user(self):
        delete_response = requests.request("DELETE", base_url + users_list[1]["username"], headers=headers,
                                           data=payload_delete)
        return delete_response.json()["message"], delete_response.status_code

    def login_user(self):
        login_response = requests.request("GET", base_url + "login", params={"username": users_list[0]["username"],
                                                                             "password": users_list[0]["password"]},
                                          headers=headers,
                                          data=payload_delete)
        return login_response.json(), login_response.status_code

    def logout_user(self):
        logout_response = requests.request("GET", base_url + "logout", headers=headers, data=payload_delete)
        return logout_response.json(), logout_response.status_code

#
# sample_response = CreateUserRequests()
# # print(sample_response.create_users())
# print(sample_response.get_user())
# print(sample_response.put_user())
# print(sample_response.delete_user()[0])
# print(sample_response.login_user())
# print(sample_response.logout_user())
