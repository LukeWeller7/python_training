import requests
import random


def end_condition(attacker, defender):
    type_chart = {
        "normal": {"normal": "draw",
                   "fire": "draw",
                   "water": "draw",
                   "electric": "draw",
                   "grass": "draw",
                   "ice": "draw",
                   "fighting": "draw",
                   "poison": "draw",
                   "ground": "draw",
                   "flying": "draw",
                   "psychic": "draw",
                   "bug": "draw",
                   "rock": "lose",
                   "ghost": "lose",
                   "dragon": "draw",
                   "dark": "draw",
                   "steel": "lose",
                   "fairy": "draw"
                   },
        "fire": {"normal": "draw",
                 "fire": "lose",
                 "water": "lose",
                 "electric": "draw",
                 "grass": "win",
                 "ice": "win",
                 "fighting": "draw",
                 "poison": "draw",
                 "ground": "draw",
                 "flying": "draw",
                 "psychic": "draw",
                 "bug": "win",
                 "rock": "lose",
                 "ghost": "draw",
                 "dragon": "lose",
                 "dark": "draw",
                 "steel": "win",
                 "fairy": "draw"
                 },
        "water": {"normal": "draw",
                  "fire": "win",
                  "water": "lose",
                  "electric": "draw",
                  "grass": "lose",
                  "ice": "draw",
                  "fighting": "draw",
                  "poison": "draw",
                  "ground": "win",
                  "flying": "draw",
                  "psychic": "draw",
                  "bug": "draw",
                  "rock": "win",
                  "ghost": "draw",
                  "dragon": "lose",
                  "dark": "draw",
                  "steel": "draw",
                  "fairy": "draw"
                  },
        "electric": {"normal": "draw",
                     "fire": "draw",
                     "water": "win",
                     "electric": "lose",
                     "grass": "lose",
                     "ice": "draw",
                     "fighting": "draw",
                     "poison": "draw",
                     "ground": "lose",
                     "flying": "win",
                     "psychic": "draw",
                     "bug": "draw",
                     "rock": "draw",
                     "ghost": "draw",
                     "dragon": "lose",
                     "dark": "draw",
                     "steel": "draw",
                     "fairy": "draw"
                     },
        "grass": {"normal": "draw",
                  "fire": "lose",
                  "water": "win",
                  "electric": "draw",
                  "grass": "lose",
                  "ice": "draw",
                  "fighting": "draw",
                  "poison": "lose",
                  "ground": "win",
                  "flying": "lose",
                  "psychic": "draw",
                  "bug": "lose",
                  "rock": "win",
                  "ghost": "draw",
                  "dragon": "lose",
                  "dark": "draw",
                  "steel": "lose",
                  "fairy": "draw"
                  },
        "ice": {"normal": "draw",
                "fire": "draw",
                "water": "lose",
                "electric": "draw",
                "grass": "win",
                "ice": "lose",
                "fighting": "draw",
                "poison": "draw",
                "ground": "draw",
                "flying": "win",
                "psychic": "draw",
                "bug": "draw",
                "rock": "draw",
                "ghost": "draw",
                "dragon": "win",
                "dark": "draw",
                "steel": "lose",
                "fairy": "draw"
                },
        "fighting": {"normal": "win",
                     "fire": "draw",
                     "water": "draw",
                     "electric": "draw",
                     "grass": "draw",
                     "ice": "win",
                     "fighting": "draw",
                     "poison": "lose",
                     "ground": "draw",
                     "flying": "lose",
                     "psychic": "lose",
                     "bug": "lose",
                     "rock": "win",
                     "ghost": "lose",
                     "dragon": "draw",
                     "dark": "win",
                     "steel": "win",
                     "fairy": "lose"
                     },
        "poison": {"normal": "draw",
                   "fire": "draw",
                   "water": "draw",
                   "electric": "draw",
                   "grass": "win",
                   "ice": "draw",
                   "fighting": "draw",
                   "poison": "lose",
                   "ground": "lose",
                   "flying": "draw",
                   "psychic": "draw",
                   "bug": "win",
                   "rock": "lose",
                   "ghost": "lose",
                   "dragon": "draw",
                   "dark": "draw",
                   "steel": "lose",
                   "fairy": "win"
                   },
        "ground": {"normal": "draw",
                   "fire": "win",
                   "water": "draw",
                   "electric": "win",
                   "grass": "lose",
                   "ice": "draw",
                   "fighting": "draw",
                   "poison": "win",
                   "ground": "draw",
                   "flying": "lose",
                   "psychic": "draw",
                   "bug": "lose",
                   "rock": "win",
                   "ghost": "draw",
                   "dragon": "draw",
                   "dark": "draw",
                   "steel": "win",
                   "fairy": "draw"
                   },
        "flying": {"normal": "draw",
                   "fire": "draw",
                   "water": "draw",
                   "electric": "lose",
                   "grass": "win",
                   "ice": "draw",
                   "fighting": "win",
                   "poison": "draw",
                   "ground": "draw",
                   "flying": "draw",
                   "psychic": "draw",
                   "bug": "win",
                   "rock": "lose",
                   "ghost": "draw",
                   "dragon": "draw",
                   "dark": "draw",
                   "steel": "lose",
                   "fairy": "draw"
                   },
        "psychic": {"normal": "draw",
                    "fire": "draw",
                    "water": "draw",
                    "electric": "draw",
                    "grass": "draw",
                    "ice": "draw",
                    "fighting": "win",
                    "poison": "win",
                    "ground": "draw",
                    "flying": "draw",
                    "psychic": "lose",
                    "bug": "draw",
                    "rock": "draw",
                    "ghost": "draw",
                    "dragon": "draw",
                    "dark": "lose",
                    "steel": "lose",
                    "fairy": "draw"
                    },
        "bug": {"normal": "draw",
                "fire": "lose",
                "water": "draw",
                "electric": "draw",
                "grass": "win",
                "ice": "draw",
                "fighting": "lose",
                "poison": "win",
                "ground": "draw",
                "flying": "lose",
                "psychic": "win",
                "bug": "draw",
                "rock": "draw",
                "ghost": "lose",
                "dragon": "draw",
                "dark": "win",
                "steel": "lose",
                "fairy": "lose"
                },
        "rock": {"normal": "draw",
                 "fire": "win",
                 "water": "draw",
                 "electric": "draw",
                 "grass": "draw",
                 "ice": "win",
                 "fighting": "lose",
                 "poison": "draw",
                 "ground": "lose",
                 "flying": "win",
                 "psychic": "draw",
                 "bug": "win",
                 "rock": "draw",
                 "ghost": "draw",
                 "dragon": "draw",
                 "dark": "draw",
                 "steel": "lose",
                 "fairy": "draw"
                 },
        "ghost": {"normal": "draw",
                  "fire": "draw",
                  "water": "draw",
                  "electric": "draw",
                  "grass": "draw",
                  "ice": "draw",
                  "fighting": "draw",
                  "poison": "draw",
                  "ground": "draw",
                  "flying": "draw",
                  "psychic": "draw",
                  "bug": "draw",
                  "rock": "draw",
                  "ghost": "win",
                  "dragon": "draw",
                  "dark": "lose",
                  "steel": "draw",
                  "fairy": "draw"
                  },
        "dragon": {"normal": "draw",
                   "fire": "draw",
                   "water": "draw",
                   "electric": "draw",
                   "grass": "draw",
                   "ice": "draw",
                   "fighting": "draw",
                   "poison": "draw",
                   "ground": "draw",
                   "flying": "draw",
                   "psychic": "draw",
                   "bug": "draw",
                   "rock": "draw",
                   "ghost": "draw",
                   "dragon": "win",
                   "dark": "draw",
                   "steel": "lose",
                   "fairy": "lose"
                   },
        "dark": {"normal": "draw",
                 "fire": "draw",
                 "water": "draw",
                 "electric": "draw",
                 "grass": "draw",
                 "ice": "draw",
                 "fighting": "lose",
                 "poison": "draw",
                 "ground": "draw",
                 "flying": "draw",
                 "psychic": "win",
                 "bug": "draw",
                 "rock": "draw",
                 "ghost": "win",
                 "dragon": "draw",
                 "dark": "lose",
                 "steel": "draw",
                 "fairy": "lose"
                 },
        "steel": {"normal": "draw",
                  "fire": "lose",
                  "water": "lose",
                  "electric": "lose",
                  "grass": "draw",
                  "ice": "win",
                  "fighting": "draw",
                  "poison": "draw",
                  "ground": "draw",
                  "flying": "draw",
                  "psychic": "draw",
                  "bug": "draw",
                  "rock": "win",
                  "ghost": "draw",
                  "dragon": "draw",
                  "dark": "draw",
                  "steel": "lose",
                  "fairy": "win"
                  },
        "fairy": {"normal": "draw",
                  "fire": "lose",
                  "water": "draw",
                  "electric": "draw",
                  "grass": "draw",
                  "ice": "draw",
                  "fighting": "win",
                  "poison": "lose",
                  "ground": "draw",
                  "flying": "draw",
                  "psychic": "draw",
                  "bug": "draw",
                  "rock": "draw",
                  "ghost": "draw",
                  "dragon": "win",
                  "dark": "win",
                  "steel": "lose",
                  "fairy": "draw"
                  }
    }
    condition = type_chart[attacker][defender]
    print(f"Attacker {condition}")


# request_poke = requests.get("https://pokeapi.co/api/v2/pokemon-species/?limit=151")
# poke_content = request_poke.content.split()
# poke_data = request_poke.json()
# print(poke_data)
# data = poke_data["results"]
# print(request_poke)
# print(poke_content)
#
# random_poke = random.choice(data)
# pokemon_name = random_poke["name"]
#
# print(pokemon_name)
#
# print(request_poke.status_code)

request_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon-species/?limit=151")
pokemon_content = request_pokemon.json()
# print(pokemon_content)
pokemon_data = pokemon_content["results"]

pokemon_names = []
for index in range(0, 151):
    pokemon_names.append(pokemon_data[index]["name"])
#     print(pokemon_names[index])

print(f"Pokemon to choose from: {pokemon_names}")

user_choosing = True
while user_choosing:
    user_input = input()
    user_pokemon = user_input.lower()
    if user_pokemon in pokemon_names:
        user_choosing = False
    else:
        print("Invalid, please try again")

ai_pokemon = random.choice(pokemon_names)

user_pokemon_request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_names.index(user_pokemon) + 1}")
user_pokemon_content = user_pokemon_request.json()
user_pokemon_stats = user_pokemon_content["types"][0]["type"]["name"]
print(f"Your pokemon: {user_pokemon}, type: {user_pokemon_stats}")

ai_pokemon_request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_names.index(ai_pokemon) + 1}")
ai_pokemon_content = ai_pokemon_request.json()
ai_pokemon_stats = ai_pokemon_content["types"][0]["type"]["name"]
print(f"Ai Pokemon: {ai_pokemon}, tpye {ai_pokemon_stats}")

move_order = random.randint(0, 1)
if move_order == 0:
    print("You attacked first:")
    end_condition(user_pokemon_stats, ai_pokemon_stats)
elif move_order == 1:
    print("Ai attacked first:")
    end_condition(ai_pokemon_stats, user_pokemon_stats)

# "stats":[{"base_stat":60,"effort":0,"stat":{"name":"hp","url":"https://pokeapi.co/api/v2/stat/1/"}},{"base_stat":62,"effort":0,"stat":{"name":"attack","url":"https://pokeapi.co/api/v2/stat/2/"}},{"base_stat":63,"effort":0,"stat":{"name":"defense","url":"https://pokeapi.co/api/v2/stat/3/"}},{"base_stat":80,"effort":1,"stat":{"name":"special-attack","url":"https://pokeapi.co/api/v2/stat/4/"}},{"base_stat":80,"effort":1,"stat":{"name":"special-defense","url":"https://pokeapi.co/api/v2/stat/5/"}},{"base_stat":60,"effort":0,"stat":{"name":"speed","url":"https://pokeapi.co/api/v2/stat/6/"}}]
# print(pokemon_data)
