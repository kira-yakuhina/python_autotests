import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ca4a6eabc4b9ab42b796c11b7372c3f8'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
body_new_pokemon = {
    "name": "Василиса",
    "photo_id": 908
}
response_new_pokemon = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_new_pokemon)
ID = response_new_pokemon.json()['id']

new_name_pokemon = {
    "pokemon_id": ID,
    "name": "Невинная Ромашка",
    "photo_id": 906
}
body_new_name_pokemon = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=new_name_pokemon)

pokemon_in_pokeball = {
    "pokemon_id": ID
}

body_pokemon_in_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=pokemon_in_pokeball)
print(body_pokemon_in_pokeball)

