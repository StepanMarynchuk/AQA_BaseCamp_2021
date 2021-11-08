import requests
from data import *

payload = {}


class ApiRequests():

    def __str__(self):
        return self.get()

    def get(self):
        get_response = requests.request("GET", base_url + get_endpoint, headers=headers, data=payload)
        return get_response.text, get_response.status_code

    def post(self):
        post_response = requests.request("POST", base_url + post_endpoint, headers=headers, data=payload)
        return post_response.headers.get('Content-Length'), post_response.status_code

    def put(self):
        put_response = requests.request("PUT", base_url + put_endpoint, headers=headers, data=payload)
        return put_response.json()["headers"]["host"], put_response.status_code


sample_response = ApiRequests()
print(sample_response.get())
print(sample_response.post())
print(sample_response.put())
