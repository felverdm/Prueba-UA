class Pokemon:
    def __init__(self, id, name, abilities, sprites, types):
        self.id = id
        self.name = name
        self.abilities = [Ability(a['ability']['name'], a['ability']['url'], a['is_hidden'], a['slot']) for a in abilities]
        self.sprites = Sprites(sprites['back_default'], sprites['back_shiny'], sprites['front_default'], sprites['front_shiny'])
        self.types = [Type(t['type']['name'], t['type']['url'], t['slot']) for t in types]

class Ability:
    def __init__(self, name, url, is_hidden, slot):
        self.name = name
        self.url = url
        self.is_hidden = is_hidden
        self.slot = slot

class Sprites:
    def __init__(self, back_default, back_shiny, front_default, front_shiny):
        self.back_default = back_default
        self.back_shiny = back_shiny
        self.front_default = front_default
        self.front_shiny = front_shiny

class Type:
    def __init__(self, name, url, slot):
        self.name = name
        self.url = url
        self.slot = slot