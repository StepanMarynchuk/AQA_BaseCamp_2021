import json

base_url = "https://petstore.swagger.io/v2/user/"
# endpoints
create_users_endpoint = "createWithList"
logout_endpoint = "logout"

# header
headers = {
    'Content-Type': 'application/json'
}

# users lists
users_list = [
    {
        "id": 9,
        "username": "Stepan",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    },
    {
        "id": 10,
        "username": "Marta",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
]

new_users_data = {
    "id": 22,
    "username": "Stepan",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
}

# payload
payload_update = json.dumps(new_users_data)
payload_delete = ""
payload = json.dumps(users_list)
