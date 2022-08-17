import requests


class TestUserAPI:

    def test_user(self):
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }

        data_user = {
            "id": 0,
            "username": "AndreiSavchuk",
            "firstName": "Andrei",
            "lastName": "Savchuk",
            "email": "string",
            "password": "12345678",
            "phone": "375291111111",
            "userStatus": 0
        }

        data_user_2 = {
            "id": 9222968140497200018,
            "username": "KarolSav",
            "firstName": "Andrey",
            "lastName": "Sauchuk",
            "email": "string",
            "password": "12345678",
            "phone": "375291111111",
            "userStatus": 0
        }

        response_post = requests.post('https://petstore.swagger.io/v2/user', json=data_user, headers=headers)
        print(response_post.json())
        print(response_post)
        print()

        response_get = requests.get(f"https://petstore.swagger.io/v2/user/AndreiSavchuk")
        print(response_get.json())
        print(response_get)
        assert response_get.json()["username"] == 'AndreiSavchuk', "User not added"
        print()

        response_put = requests.put(f"https://petstore.swagger.io/v2/user/AndreiSavchuk", json=data_user_2,
                                    headers=headers)
        print(response_put.json())
        print(response_put)
        print()

        response_get = requests.get(f"https://petstore.swagger.io/v2/user/KarolSav")
        print(response_get.json())
        print(response_get)
        assert response_get.json()["username"] == "KarolSav", "User dont changed"
        print()
