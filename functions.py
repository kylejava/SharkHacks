import requests
import json
from pprint import pprint

def get_pokemon(tweet):
    types = ""
    birthday = obtain_date(tweet)
    index = get_pokemon_index(birthday)
    url = "https://pokeapi.co/api/v2/pokemon/"+ str(index)
    resp = requests.get(url)
    data = resp.json()
    name = data['name'].capitalize()
    for i in range(len(data['types'])):
        type = data['types'][i]['type']['name']
        type = type.capitalize()
        types += type + " "
    pokemon = {
        'name': name,
        'index': str(index),
        'type': types,
        'photo':data['sprites']['other']['official-artwork']['front_default'],

    }
    pic = requests.get(pokemon['photo'])
    file = open("pokemon.png", "wb")
    file.write(pic.content)
    file.close()
    return pokemon


#get get_pokemon_index, (month, day, year) and mod by 4
def get_pokemon_index(birthday):
    x = (birthday) % 898
    if x == 0:
        x = x+1
        return x
    elif x != 0:
        return x


def return_birthday(queue):
    current_num = ""
    num_arr = []
    for i in range(len(queue)):
        if(queue[i].isdigit()):
            current_num += queue[i]
        else:
            num_arr.append(current_num)
            current_num = ""
    num_arr.append(current_num)
    return num_arr


def obtain_date(s):
    num_arr = []
    queue = []
    birthday = 0
    for i in range(len(s)):
        if(s[i].isdigit() or s[i] == '/'):
            queue.append(s[i])
    num_arr = return_birthday(queue)
    for i in range(len(num_arr)):
        num = int(num_arr[i])
        birthday += num

    return birthday

s = "3/15/2000"
get_pokemon(s)
