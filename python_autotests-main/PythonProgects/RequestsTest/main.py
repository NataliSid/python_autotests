import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'a8d37472935d7fc52a836633202077c7'
HEADER = {'Content-Type':'application/json', 'trainer token':TOKEN}

body_registration = {
    "trainer_token":TOKEN,
    "email":"naila.shirokova@yandex.ru",
    "password":"kol56Bosa"
}


body_create = {
    "name": "Бульбазавр",
    "photo" : "https://dolnikov.ru/pokemons/albums/001.png"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)	
print(response_create.text)
