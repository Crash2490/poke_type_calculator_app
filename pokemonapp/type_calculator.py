class Pokemon:
    """Pocket Monster."""

    TYPES = ['normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy']
    
    dfnd_agnst_typ_val_lst = {'normal': {'fighting': 2, 'normal': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'bug': 1, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'ghost': 0},
        'fire': {'water': 2, 'rock': 2, 'ground': 2, 'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ghost': 1, 'electric': 1, 'psychic': 1, 'dragon': 1, 'dark': 1, 'bug': .5, 'steel': .5, 'fire': .5, 'ice': .5, 'grass': .5, 'fairy': .5},
        'water': {'electric': 2, 'grass': 2, 'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 1, 'psychic': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'steel': .5, 'fire': .5, 'water': .5, 'ice': .5},
        'electric': {'ground': 2, 'normal': 1, 'fighting': 1, 'poison': 1, 'rock': 1, 'bug': 1, 'ghost': 1, 'fire': 1, 'water': 1, 'grass': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'flying': .5, 'steel': .5, 'electric': .5},
        'grass': {'fire': 2, 'ice': 2, 'poison': 2, 'flying': 2, 'bug': 2, 'normal': 1, 'fighting': 1, 'rock': 1, 'ghost': 1, 'steel': 1, 'psychic': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'ground': .5, 'water': .5, 'grass': .5, 'electric': .5},
        'ice': {'fire': 2, 'fighting': 2, 'rock': 2, 'steel': 2, 'normal': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'bug': 1, 'ghost': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'ice': .5},
        'fighting': {'flying': 2, 'psychic': 2, 'fairy': 2, 'normal': 1, 'fighting': 1, 'poison': 1, 'ground': 1, 'ghost': 1, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'dragon': 1, 'rock': .5, 'bug': .5, 'dark': .5},
        'poison': {'ground': 2, 'psychic': 2, 'normal': 1, 'flying': 1, 'rock': 1, 'ghost': 1, 'steel': 1, 'fire': 1, 'water': 1, 'electric': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fighting': .5, 'poison': .5, 'bug': .5, 'grass': .5, 'fairy': .5},
        'ground': {'water': 2, 'grass': 2, 'ice': 2, 'normal': 1, 'fighting': 1, 'flying': 1, 'ground': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'fire': 1, 'psychic': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'poison': .5, 'rock': .5, 'electric': 0},
        'flying': {'electric': 2, 'ice': 2, 'rock': 2, 'normal': 1, 'flying': 1, 'poison': 1, 'ghost': 1, 'steel': 1, 'fire': 1, 'water': 1, 'psychic': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'fighting': .5, 'bug': .5, 'grass': .5, 'ground': 0},
        'psychic': {'bug': 2, 'ghost': 2, 'dark': 2, 'normal': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'dragon': 1, 'fairy': 1, 'fighting': .5, 'psychic': .5},
        'bug': {'fire': 2, 'flying': 2, 'rock': 2, 'normal': 1, 'poison': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'water': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'fighting': .5, 'ground': .5, 'grass': .5},
        'rock': {'water': 2, 'grass': 2, 'fighting': 2, 'ground': 2, 'steel': 2, 'rock': 1, 'bug': 1, 'ghost': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'dark': 1, 'fairy': 1, 'normal': .5, 'flying': .5, 'poison': .5, 'fire': .5},
        'ghost': {'ghost': 2, 'dark': 2, 'flying': 1, 'ground': 1, 'rock': 1, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'dragon': 1, 'fairy': 1, 'poison': .5, 'bug': .5, 'normal': 0, 'fighting': 0},
        'dragon': {'ice': 2, 'dragon': 2, 'fairy': 2, 'normal': 1, 'fighting': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'bug': 1, 'ghost': 1, 'steel': 1, 'psychic': 1, 'dark': 1, 'fire': .5, 'water': .5, 'grass': .5, 'electric': .5},
        'dark': {'fighting': 2, 'bug': 2, 'fairy': 2, 'normal': 1, 'flying': 1, 'poison': 1, 'ground': 1, 'rock': 1, 'steel': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'ice': 1, 'dragon': 1, 'ghost': .5, 'dark': .5, 'psychic': 0},
        'steel': {'fire': 2, 'fighting': 2, 'ground': 2, 'ghost': 1, 'water': 1, 'electric': 1, 'dark': 1, 'normal': .5, 'flying': .5, 'rock': .5, 'bug': .5, 'steel': .5, 'grass': .5, 'psychic': .5, 'ice': .5, 'dragon': .5, 'fairy': .5, 'poison': 0},
        'fairy': {'poison': 2, 'steel': 2, 'normal': 1, 'flying': 1, 'ground': 1, 'rock': 1, 'ghost': 1, 'fire': 1, 'water': 1, 'grass': 1, 'electric': 1, 'psychic': 1, 'ice': 1, 'fairy': 1, 'fighting': .5, 'bug': .5, 'dark': .5, 'dragon': 0}}

    VOWELS = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, name, type1, type2=None):
        self.name = name
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        if self.type2 == None:
            if self.type1[0] not in self.VOWELS:
                return "{} is a {} type pokemon.".format(self.name, self.type1)
            else:
                return "{} is an {} type pokemon.".format(self.name, self.type1)
        elif self.type2 != None:
            if self.type1[0] not in self.VOWELS:
                return "{} is a {}/{} type pokemon.".format(self.name, self.type1, self.type2)
            else:
                return "{} is an {}/{} type pokemon.".format(self.name, self.type1, self.type2)

    def DualTypeCalc(self, type1_dict, type2_dict):
        dualtype_val_dict = {}
        for k in type1_dict:
            if k in type2_dict:
                dualtype_val_dict[k] = type1_dict[k]*type2_dict[k]
        return dualtype_val_dict

    def Weakness(self):
        """Takes Pokemon and returns the types that it is weak against."""

        if self.type2 != None:
            t1_dict = self.dfnd_agnst_typ_val_lst[self.type1]
            t2_dict = self.dfnd_agnst_typ_val_lst[self.type2]
            dualtype_val_dict = self.DualTypeCalc(t1_dict, t2_dict)
            weak_agnst = [k for k in dualtype_val_dict if dualtype_val_dict[k] >= 2]
            print("{}/{} is weak against {}.".format(self.type1, self.type2, weak_agnst))
        elif self.type2 == None:
            type_vals = self.dfnd_agnst_typ_val_lst[self.type1]
            weak_agnst = [k for k in type_vals if type_vals[k]==2]
            print("{} is weak against {}.".format(self.type1, weak_agnst))



pokemon = Pokemon('beldum', 'steel', 'psychic')
print(pokemon)
pokemon.Weakness()

pokemon_2 = Pokemon('palpitoad', 'water', 'ground')
print(pokemon_2)
pokemon_2.Weakness()

pokemon_3 = Pokemon('frosmoth', 'ice', 'bug')
print(pokemon_3)
pokemon_3.Weakness()

pokemon_4 = Pokemon('thundurus', 'electric', 'flying')
print(pokemon_4)
pokemon_4.Weakness()

pokemon_5 = Pokemon('applin', 'grass', 'dragon')
print(pokemon_5)
pokemon_5.Weakness()