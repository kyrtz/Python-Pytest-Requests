import requests 

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8a39dba61cec9e76be94aac1fdd5eef3'
HEADER = {'Content-Type': 'application/json', 'trainer_token' : TOKEN}

body_registration =  {
                     "trainer_token": TOKEN,
                     "email": "vip@pokemon.ru",
                     "password": "Iloveqa1"
                     }

body_confirmation =  {
                     "trainer_token" : TOKEN
                     }

body_rename =        {
                     "pokemon_id": "12331",
                     "name": "New Name",
                     "photo_id": 2
                     }

body_addpokeball =   {
                     "pokemon_id": "9"
                     }

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration )
print(response.text)'''

'''response_confirmation = requests.post (url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation )
print(response_confirmation.text)'''

'''response_rename = requests.put (url = f'{URL}/pokemons', headers = HEADER, json = body_rename )
print(response_rename.text)'''

'''response_addpokeball = requests.post(url = f'{URL}/trainers/add_pokeball ', headers = HEADER, json = body_addpokeball )
print(response_addpokeball.text)'''

