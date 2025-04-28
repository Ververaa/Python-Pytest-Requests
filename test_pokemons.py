import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b133530d8f3751ac249348e0199b6479'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 29246

def test_status_code():
    response = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response(): 
    response_get = requests.get(url = f'{URL}/v2/pokemons', params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]['name']== 'swirlix'
