import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b133530d8f3751ac249348e0199b6479'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}

body_create_pokemons = {
    "name": "generate",
    "photo_id": -1
}

body_name_change = {
    "pokemon_id": "",
    "name": "New Name"
}

body_trainers_add_pokeball = {
    "pokemon_id": "id"
    }

response = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create_pokemons)
print(response.text)

pokemon_id = response.json()['id']

response_name_change = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_name_change)
print (response_name_change.text)

response_trainers_add_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_trainers_add_pokeball)
print (response_trainers_add_pokeball.text)