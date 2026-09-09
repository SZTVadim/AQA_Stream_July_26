import random

import requests

BASE_URL = "https://petstore.swagger.io/"
ENDPOINT = "v2/pet/"
HEADERS = {"accept": "application/json"}

def receive_json_for_create(id_pet, category_id_pet, category_pet_name, pet_name, photo_pet, tags_id, personality_pet,
                            status):
    return {
        "id": id_pet,
        "category": {"id": category_id_pet, "name": category_pet_name},
        "name": pet_name,
        "photoUrls": [photo_pet],
        "tags": [{"id": tags_id, "name": personality_pet}],
        "status": status
    }


photo_pet_1 = "https://avatars.mds.yandex.net/i?id=9076ba718c33893b2a67c03c4d412caa3cf16f58-5320607-images-thumbs&n=13"
photo_pet_2 = "https://avatars.mds.yandex.net/i?id=6d1c911b8dc680c20870908e9549c45c89489102-5858835-images-thumbs&n=13"

data_pet_1 = receive_json_for_create(random.randint(10000000, 99999999), 7, "Cat",
                                     "Tishka", photo_pet_1, 7, "friendly",
                                     "pending")


def create_pet():
    response = requests.post(f"{BASE_URL}{ENDPOINT}", headers=HEADERS, json=data_pet_1)
    return response

response_create_pet = create_pet()
res_id_pet = response_create_pet.json()["id"]
print(response_create_pet)
print(response_create_pet.status_code)
print(response_create_pet.json())

def get_pet(id_pet):
    response = requests.get(f"{BASE_URL}{ENDPOINT}{id_pet}", headers=HEADERS)
    return response

response_get_pet = get_pet(res_id_pet)
print(response_get_pet)
print(response_get_pet.status_code)
print(response_get_pet.json())

def put_pet(id_pet):
    update_pet_data = receive_json_for_create(id_pet, 6, "Kot",
                                     "Barsik", photo_pet=photo_pet_2, tags_id=6, personality_pet="agressive",
                                     status="available")
    response = requests.put(f"{BASE_URL}{ENDPOINT}", headers=HEADERS, json=update_pet_data)
    return response

response_put_pet = put_pet(res_id_pet)
print(response_put_pet)
print(response_put_pet.status_code)
print(response_put_pet.json())

def delete_pet(id_pet):
    response = requests.delete(f"{BASE_URL}{ENDPOINT}{id_pet}", headers=HEADERS)
    return response

response_delete_pet = delete_pet(res_id_pet)
print(response_delete_pet.status_code)
print(response_delete_pet.json())

print(get_pet(res_id_pet))