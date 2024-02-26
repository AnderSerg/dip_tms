import requests


class TestPetAPI:
    def test_pet(self):
        headers = {
            'Content-type': 'application/json',
            'api_key': 'special-key',
            'Accept': 'application/json'
        }

        data_pet = {
            "id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "Jasper",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

        response_post = requests.post('https://petstore.swagger.io/v2/pet', json=data_pet, headers=headers)
        print(response_post.json())
        print(response_post)
        print()

        pet_id = response_post.json()["id"]
        print(pet_id)
        print()

        response_get = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        print(response_get.json())
        print(response_get)
        assert response_get.json()["name"] == "Jasper", "Pet Jasper is not add"
        print()

        response_delete = requests.delete(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        print(response_delete.json())
        print(response_delete)
        print()

        response_get = requests.get(f"https://petstore.swagger.io/v2/pet/{pet_id}")
        print(response_get.json())
        print(response_get)
        assert response_get.json()["message"] == "Pet not found", "Jasper is not deleted"
        print()
