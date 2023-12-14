import pytest
from main import GetLightPokemonById, GetLightPokemonByName, GetPokemonById, GetPokemonByName

# test de que los pokemon de los ids siguientes tienen definidos sus tipos
@pytest.mark.parametrize(
    "input_id, expected",
    [
        (1, "grass"),
        (4, "fire"),
        (25, "electric"),
        (149, "dragon"),
        (150, "psychic")
    ]
)
def test_GetLightPokemonById(input_id, expected):
    #assert 1 == 1
    data = GetLightPokemonById(input_id)
    assert data.types[0].name == expected


# test de que los pokemon de los siguientes nombres tienen ids definidos
@pytest.mark.parametrize(
    "input_name, expected",
    [
        ("bulbasaur",1),
        ("charmander",4),
        ("pikachu", 25),
        ("dragonite",149),
        ("mewtwo",150)
    ]
)
def test_GetLightPokemonByName(input_name, expected):    
    #assert 1 == 1
    data = GetLightPokemonByName(input_name)
    assert data.id == expected