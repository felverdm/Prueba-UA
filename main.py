from fastapi import FastAPI
from ApiCalls import PokemonApiCall



app = FastAPI()

#http://127.0.0.1:8000

#@app.get("/")
#def index():
#    return "Hola UA"


@app.get("/test/{name}")
def test(name: str ):
    print("aqui"+name)
    return "Hola UA"+name

@app.get("/GetPokemonByName/{name}")
def GetPokemonByName(name: str ):
    data = PokemonApiCall.GetPokemonByName(name)
    return data

@app.get("/GetPokemonById/{id}")
def GetPokemonById(id: int ):
    print("clear")
    data = PokemonApiCall.GetPokemonById(id)
    return data

@app.get("/GetLigthPokemonByName/{name}")
def GetLightPokemonByName(name: str ):
    print("aqui")
    data = PokemonApiCall.GetLightPokemonByName(name)
    return data

@app.get("/GetLightPokemonById/{id}")
def GetLightPokemonById(id: int ):
    print("aqui")    
    data = PokemonApiCall.GetLightPokemonById(id)
    #print(data.types[0].name)
    return data