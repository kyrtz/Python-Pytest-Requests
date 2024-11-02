import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8a39dba61cec9e76be94aac1fdd5eef3'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 8360

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200
    