from pip._vendor import requests
import json
from application import Pokemon, db
from weakness import weakness


def get_pokemon_info_urls(url):
    resp = requests.get(url=url)
    data_dict = resp.json()
    poke_info_lst = data_dict.get('results')
    url_list = []
    for dict in poke_info_lst:
        url_list.append(dict['url'])
    return url_list


def create_pokemon_list(url_list):
    pokemon_list = []
    for pokeapi_url in url_list:
        mypokemon = Pokemon()
        r = requests.get(url=pokeapi_url)
        poke_dict = r.json()
        mypokemon.id = poke_dict['id']
        mypokemon.dex_num = poke_dict['species']['url'].split('/')[-2:-1][0]
        mypokemon.name = poke_dict['name']
        mypokemon.type1 = poke_dict['types'][0]['type']['name']
        if len(poke_dict['types']) == 2:
            mypokemon.type2 = poke_dict['types'][1]['type']['name']
        mypokemon.sprite = poke_dict['sprites']['front_default']
        mypokemon.type_values = weakness('normal', mypokemon.type1, mypokemon.type2)
        pokemon_list.append(mypokemon)
    return pokemon_list

def commit_pokemon_to_db(pokemon_list):
    for pokemon in pokemon_list:
        db.session.add(pokemon)
        print("adding {} to database.".format(pokemon))
    db.session.commit()

db.drop_all()
db.create_all()
api_url = 'https://pokeapi.co/api/v2/pokemon?limit=807'
url_list = get_pokemon_info_urls(api_url)
pokemon_list = create_pokemon_list(url_list)
commit_pokemon_to_db(pokemon_list)








