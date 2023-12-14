from fastapi import FastAPI
from ApiCalls import PokemonApiCall



app = FastAPI()

#http://127.0.0.1:8000

#@app.get("/")
#def index():
#    return "Hola UA"

#función para saber cómo filtrar
@app.get("/help")
def help( ):
    return "Hola, para filtrar los datos de los pokemon los valores son: id = 1 | nombre = 2 | habilidades = 3 | sprites = 4 | tipos = 5"

#función del api que busca toda la información del pokemon por nombre
@app.get("/GetPokemonByName/{name}")
def GetPokemonByName(name: str ):
    data = PokemonApiCall.GetPokemonByName(name) #llama a la función que llama al api de pokemon
    return data

#función del api que busca toda la información del pokemon por id
@app.get("/GetPokemonById/{id}")
def GetPokemonById(id: int ):
    print("clear")
    data = PokemonApiCall.GetPokemonById(id) #llama a la función que llama al api de pokemon
    return data

#función del api que busca parte de la información del pokemon por nombre
@app.get("/GetLigthPokemonByName/{name}")
def GetLightPokemonByName(name: str ):
    print("aqui")
    data = PokemonApiCall.GetLightPokemonByName(name) #llama a la función que llama al api de pokemon
    return data

#función del api que busca parte de la información del pokemon por id
@app.get("/GetLightPokemonById/{id}")
def GetLightPokemonById(id: int ):
    print("aqui")    
    data = PokemonApiCall.GetLightPokemonById(id) #llama a la función que llama al api de pokemon
    #print(data.types[0].name)
    return data


#función del api que filtra la información del pokemon por nombre
@app.get("/GetFilterPokemonByName/{name}/{filter}")
def GetFilterPokemonByName(name: str, filter: int):
    print("aqui")
    data = PokemonApiCall.GetFilterPokemonByName(name, filter) #llama a la función que llama al api de pokemon
    return data

#función del api que filtra la información del pokemon por id
@app.get("/GetFilterPokemonById/{id}/{filter}")
def GetFilterPokemonById(id: int, filter: int):
    print("aqui")    
    data = PokemonApiCall.GetFilterPokemonById(id, filter) #llama a la función que llama al api de pokemon
    #print(data.types[0].name)
    return data



"""
#función del api que actualiza el tipo del pokemon por id
@app.post("/SetPokemonInfoById/{id}")
def SetPokemonInfoById(id: int ):
    print("aqui")    
    rta = PokemonApiCall.SetPokemonInfoById(id) #llama a la función que llama al api de pokemon
    #print(data.types[0].name)
    return rta
"""
