import requests
import json
from collections import namedtuple
from json import JSONEncoder
from Models import PokemonModel

from types import SimpleNamespace

#base_url = "https://pokeapi.co/api/v2/"
with open('base_url.txt', 'r') as file:
    base_url = file.read()

def GetPokemonByName(name: str):
    response = requests.get(base_url+"pokemon/"+name)
    response.raise_for_status()
    data = response.json()
    return data

def GetPokemonById(id: int):
    response = requests.get(base_url+"pokemon/"+str(id))
    response.raise_for_status()
    data = response.json()
    return data

def GetLightPokemonByName(name: str):
    response = requests.get(base_url+"pokemon/"+name)
    response.raise_for_status()
    data = response.json()
    pokemonRta = PokemonModel.Pokemon(id=data["id"],
                                   name = data["name"],
                                   abilities=data["abilities"],
                                   sprites=data["sprites"],
                                   types=data["types"])
    print(pokemonRta.id)
    return pokemonRta

def GetLightPokemonById(id: int):
    response = requests.get(base_url+"pokemon/"+str(id))
    response.raise_for_status()
    data = response.json()
    pokemonRta = PokemonModel.Pokemon(id=data["id"],
                                   name = data["name"],
                                   abilities=data["abilities"],
                                   sprites=data["sprites"],
                                   types=data["types"])
    print(pokemonRta.id)
    return pokemonRta