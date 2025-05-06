import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ca4a6eabc4b9ab42b796c11b7372c3f8'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = 294

def test_list_trainers():
    response = requests.get(url=f"{URL}/trainers")
    assert response.status_code == 200

def test_presence_of_specific_trainer_in_list():
    response = requests.get(url=f"{URL}/trainers", params={"trainer_id":TRAINER_ID})
    assert response.status_code == 200