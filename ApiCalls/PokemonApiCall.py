import requests
import json
import pyodbc
from collections import namedtuple
from json import JSONEncoder
from Models import PokemonModel

from types import SimpleNamespace

#base_url = "https://pokeapi.co/api/v2/"
#busca en el archivo la url base para llamar el api de Pokemon
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
    pokemonRta = PokemonModel.Pokemon(id=data["id"], # se filtran los datos que se requieren en la respuesta corta
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
    pokemonRta = PokemonModel.Pokemon(id=data["id"], # se filtran los datos que se requieren en la respuesta corta
                                   name = data["name"],
                                   abilities=data["abilities"],
                                   sprites=data["sprites"],
                                   types=data["types"])
    print(pokemonRta.id)
    return pokemonRta


def GetFilterPokemonByName(name: str, filter: int):
    response = requests.get(base_url+"pokemon/"+name)
    response.raise_for_status()
    data = response.json()
    pokemonRta = PokemonModel.Pokemon(id=data["id"], # se filtran los datos que se requieren en la respuesta corta
                                   name = data["name"],
                                   abilities=data["abilities"],
                                   sprites=data["sprites"],
                                   types=data["types"])
    if filter == 1: #según el filtro va la respuesta
        return pokemonRta.id
    elif filter == 3:
        return pokemonRta.abilities
    elif filter == 4:
        return pokemonRta.sprites
    elif filter == 5:
        return pokemonRta.types
    else:
        return pokemonRta # si el filtro no es correcto retorna todo


def GetFilterPokemonById(id: int, filter: int):
    response = requests.get(base_url+"pokemon/"+str(id))
    response.raise_for_status()
    data = response.json()
    pokemonRta = PokemonModel.Pokemon(id=data["id"], # se filtran los datos que se requieren en la respuesta corta
                                   name = data["name"],
                                   abilities=data["abilities"],
                                   sprites=data["sprites"],
                                   types=data["types"])
    if filter == 2: #según el filtro va la respuesta
        return pokemonRta.name
    elif filter == 3:
        return pokemonRta.abilities
    elif filter == 4:
        return pokemonRta.sprites
    elif filter == 5:
        return pokemonRta.types
    else:
        return pokemonRta # si el filtro no es correcto retorna todo
    


"""
def SetPokemonInfoById(id: int):
    server = "DESKTOP-STG5LND"
    db = "PokemonUA"
    login = "sqlConn"
    password = "123"
"""