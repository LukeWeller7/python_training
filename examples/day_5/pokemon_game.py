import requests
import random
import time
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import PIL


def move_multiplier(attacker, defender):
    type_chart = {
        "normal": {"normal": 1,
                   "fire": 1,
                   "water": 1,
                   "electric": 1,
                   "grass": 1,
                   "ice": 1,
                   "fighting": 1,
                   "poison": 1,
                   "ground": 1,
                   "flying": 1,
                   "psychic": 1,
                   "bug": 1,
                   "rock": 0.5,
                   "ghost": 0.5,
                   "dragon": 1,
                   "dark": 1,
                   "steel": 0.5,
                   "fairy": 1
                   },
        "fire": {"normal": 1,
                 "fire": 0.5,
                 "water": 0.5,
                 "electric": 1,
                 "grass": 2,
                 "ice": 2,
                 "fighting": 1,
                 "poison": 1,
                 "ground": 1,
                 "flying": 1,
                 "psychic": 1,
                 "bug": 2,
                 "rock": 0.5,
                 "ghost": 1,
                 "dragon": 0.5,
                 "dark": 1,
                 "steel": 2,
                 "fairy": 1
                 },
        "water": {"normal": 1,
                  "fire": 2,
                  "water": 0.5,
                  "electric": 1,
                  "grass": 0.5,
                  "ice": 1,
                  "fighting": 1,
                  "poison": 1,
                  "ground": 2,
                  "flying": 1,
                  "psychic": 1,
                  "bug": 1,
                  "rock": 2,
                  "ghost": 1,
                  "dragon": 0.5,
                  "dark": 1,
                  "steel": 1,
                  "fairy": 1
                  },
        "electric": {"normal": 1,
                     "fire": 1,
                     "water": 2,
                     "electric": 0.5,
                     "grass": 0.5,
                     "ice": 1,
                     "fighting": 1,
                     "poison": 1,
                     "ground": 0.5,
                     "flying": 2,
                     "psychic": 1,
                     "bug": 1,
                     "rock": 1,
                     "ghost": 1,
                     "dragon": 0.5,
                     "dark": 1,
                     "steel": 1,
                     "fairy": 1
                     },
        "grass": {"normal": 1,
                  "fire": 0.5,
                  "water": 2,
                  "electric": 1,
                  "grass": 0.5,
                  "ice": 1,
                  "fighting": 1,
                  "poison": 0.5,
                  "ground": 2,
                  "flying": 0.5,
                  "psychic": 1,
                  "bug": 0.5,
                  "rock": 2,
                  "ghost": 1,
                  "dragon": 0.5,
                  "dark": 1,
                  "steel": 0.5,
                  "fairy": 1
                  },
        "ice": {"normal": 1,
                "fire": 1,
                "water": 0.5,
                "electric": 1,
                "grass": 2,
                "ice": 0.5,
                "fighting": 1,
                "poison": 1,
                "ground": 1,
                "flying": 2,
                "psychic": 1,
                "bug": 1,
                "rock": 1,
                "ghost": 1,
                "dragon": 2,
                "dark": 1,
                "steel": 0.5,
                "fairy": 1
                },
        "fighting": {"normal": 2,
                     "fire": 1,
                     "water": 1,
                     "electric": 1,
                     "grass": 1,
                     "ice": 2,
                     "fighting": 1,
                     "poison": 0.5,
                     "ground": 1,
                     "flying": 0.5,
                     "psychic": 0.5,
                     "bug": 0.5,
                     "rock": 2,
                     "ghost": 0.5,
                     "dragon": 1,
                     "dark": 2,
                     "steel": 2,
                     "fairy": 0.5
                     },
        "poison": {"normal": 1,
                   "fire": 1,
                   "water": 1,
                   "electric": 1,
                   "grass": 2,
                   "ice": 1,
                   "fighting": 1,
                   "poison": 0.5,
                   "ground": 0.5,
                   "flying": 1,
                   "psychic": 1,
                   "bug": 2,
                   "rock": 0.5,
                   "ghost": 0.5,
                   "dragon": 1,
                   "dark": 1,
                   "steel": 0.5,
                   "fairy": 2
                   },
        "ground": {"normal": 1,
                   "fire": 2,
                   "water": 1,
                   "electric": 2,
                   "grass": 0.5,
                   "ice": 1,
                   "fighting": 1,
                   "poison": 2,
                   "ground": 1,
                   "flying": 0.5,
                   "psychic": 1,
                   "bug": 0.5,
                   "rock": 2,
                   "ghost": 1,
                   "dragon": 1,
                   "dark": 1,
                   "steel": 2,
                   "fairy": 1
                   },
        "flying": {"normal": 1,
                   "fire": 1,
                   "water": 1,
                   "electric": 0.5,
                   "grass": 2,
                   "ice": 1,
                   "fighting": 2,
                   "poison": 1,
                   "ground": 1,
                   "flying": 1,
                   "psychic": 1,
                   "bug": 2,
                   "rock": 0.5,
                   "ghost": 1,
                   "dragon": 1,
                   "dark": 1,
                   "steel": 0.5,
                   "fairy": 1
                   },
        "psychic": {"normal": 1,
                    "fire": 1,
                    "water": 1,
                    "electric": 1,
                    "grass": 1,
                    "ice": 1,
                    "fighting": 2,
                    "poison": 2,
                    "ground": 1,
                    "flying": 1,
                    "psychic": 0.5,
                    "bug": 1,
                    "rock": 1,
                    "ghost": 1,
                    "dragon": 1,
                    "dark": 0.5,
                    "steel": 0.5,
                    "fairy": 1
                    },
        "bug": {"normal": 1,
                "fire": 0.5,
                "water": 1,
                "electric": 1,
                "grass": 2,
                "ice": 1,
                "fighting": 0.5,
                "poison": 2,
                "ground": 1,
                "flying": 0.5,
                "psychic": 2,
                "bug": 1,
                "rock": 1,
                "ghost": 0.5,
                "dragon": 1,
                "dark": 2,
                "steel": 0.5,
                "fairy": 0.5
                },
        "rock": {"normal": 1,
                 "fire": 2,
                 "water": 1,
                 "electric": 1,
                 "grass": 1,
                 "ice": 2,
                 "fighting": 0.5,
                 "poison": 1,
                 "ground": 0.5,
                 "flying": 2,
                 "psychic": 1,
                 "bug": 2,
                 "rock": 1,
                 "ghost": 1,
                 "dragon": 1,
                 "dark": 1,
                 "steel": 0.5,
                 "fairy": 1
                 },
        "ghost": {"normal": 1,
                  "fire": 1,
                  "water": 1,
                  "electric": 1,
                  "grass": 1,
                  "ice": 1,
                  "fighting": 1,
                  "poison": 1,
                  "ground": 1,
                  "flying": 1,
                  "psychic": 1,
                  "bug": 1,
                  "rock": 1,
                  "ghost": 2,
                  "dragon": 1,
                  "dark": 0.5,
                  "steel": 1,
                  "fairy": 1
                  },
        "dragon": {"normal": 1,
                   "fire": 1,
                   "water": 1,
                   "electric": 1,
                   "grass": 1,
                   "ice": 1,
                   "fighting": 1,
                   "poison": 1,
                   "ground": 1,
                   "flying": 1,
                   "psychic": 1,
                   "bug": 1,
                   "rock": 1,
                   "ghost": 1,
                   "dragon": 2,
                   "dark": 1,
                   "steel": 0.5,
                   "fairy": 0.5
                   },
        "dark": {"normal": 1,
                 "fire": 1,
                 "water": 1,
                 "electric": 1,
                 "grass": 1,
                 "ice": 1,
                 "fighting": 0.5,
                 "poison": 1,
                 "ground": 1,
                 "flying": 1,
                 "psychic": 2,
                 "bug": 1,
                 "rock": 1,
                 "ghost": 2,
                 "dragon": 1,
                 "dark": 0.5,
                 "steel": 1,
                 "fairy": 0.5
                 },
        "steel": {"normal": 1,
                  "fire": 0.5,
                  "water": 0.5,
                  "electric": 0.5,
                  "grass": 1,
                  "ice": 2,
                  "fighting": 1,
                  "poison": 1,
                  "ground": 1,
                  "flying": 1,
                  "psychic": 1,
                  "bug": 1,
                  "rock": 2,
                  "ghost": 1,
                  "dragon": 1,
                  "dark": 1,
                  "steel": 0.5,
                  "fairy": 2
                  },
        "fairy": {"normal": 1,
                  "fire": 0.5,
                  "water": 1,
                  "electric": 1,
                  "grass": 1,
                  "ice": 1,
                  "fighting": 2,
                  "poison": 0.5,
                  "ground": 1,
                  "flying": 1,
                  "psychic": 1,
                  "bug": 1,
                  "rock": 1,
                  "ghost": 1,
                  "dragon": 2,
                  "dark": 2,
                  "steel": 0.5,
                  "fairy": 1
                  }
    }
    multiplier = type_chart[attacker][defender]
    return multiplier


def move_effectiveness(multiplier):  # include types to specify what types are effective against each other
    if multiplier == 2:
        return "This move is super effective, you deal double damage"
    elif multiplier == 1:
        return "This move is effective, deal regular damage"
    elif multiplier == 0.5:
        return "This move is not effective, deal half damage"
    elif multiplier == 0:
        return "This move deals no effective, deal zero damage"


def pokemon_stats(pokemon_name):
    pokemon_request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_names.index(pokemon_name) + 1}")
    pokemon_content = pokemon_request.json()
    type = pokemon_content["types"][0]["type"]["name"]

    hp = pokemon_content["stats"][0]["base_stat"]
    attack = pokemon_content["stats"][1]["base_stat"]
    defence = pokemon_content["stats"][2]["base_stat"]
    speed = pokemon_content["stats"][5]["base_stat"]
    return [pokemon_name, type, hp, attack, defence, speed]


def move_order(user_speed, ai_speed):
    if user_speed > ai_speed:
        return "user_first"
    elif user_speed < ai_speed:
        return "ai_first"
    elif user_speed == ai_speed:
        random_turn = random.randint(0, 1)
        if random_turn == 0:
            return "user_first"
        elif random_turn == 1:
            return "ai_first"


def move_power(url):
    power_request = requests.get(str(url))
    power_json = power_request.json()
    move_power_request = power_json["power"]
    return move_power_request


def move_accuracy(url):
    accuracy_request = requests.get(url)
    accuracy_json = accuracy_request.json()
    move_accuracy_request = accuracy_json["accuracy"]
    return move_accuracy_request


def move_type(url):
    type_request = requests.get(url)
    type_json = type_request.json()
    move_type_request = type_json["type"]["name"]
    return move_type_request


def move_options(pokemon_name):
    pokemon_request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_names.index(pokemon_name) + 1}")
    pokemon_content = pokemon_request.json()
    # print(pokemon_content["moves"][0]["move"]["url"])

    moves = []
    total = 0
    while total != 4:
        move_selection = random.randint(0, len(pokemon_content["moves"]) - 1)
        if move_selection in moves:
            total = total
        elif move_power(pokemon_content["moves"][move_selection]["move"]["url"]) is None:
            total = total
        elif move_accuracy(pokemon_content["moves"][move_selection]["move"]["url"]) is None:
            total = total
        else:
            moves.append(move_selection)
            total += 1

    move_1 = {
        "name": pokemon_content["moves"][moves[0]]["move"]["name"],
        "power": move_power(pokemon_content["moves"][moves[0]]["move"]["url"]),
        "accuracy": move_accuracy(pokemon_content["moves"][moves[0]]["move"]["url"]),
        "type": move_type(pokemon_content["moves"][moves[0]]["move"]["url"])
    }
    move_2 = {
        "name": pokemon_content["moves"][moves[1]]["move"]["name"],
        "power": move_power(pokemon_content["moves"][moves[1]]["move"]["url"]),
        "accuracy": move_accuracy(pokemon_content["moves"][moves[1]]["move"]["url"]),
        "type": move_type(pokemon_content["moves"][moves[1]]["move"]["url"])
    }
    move_3 = {
        "name": pokemon_content["moves"][moves[2]]["move"]["name"],
        "power": move_power(pokemon_content["moves"][moves[2]]["move"]["url"]),
        "accuracy": move_accuracy(pokemon_content["moves"][moves[2]]["move"]["url"]),
        "type": move_type(pokemon_content["moves"][moves[2]]["move"]["url"])
    }
    move_4 = {
        "name": pokemon_content["moves"][moves[3]]["move"]["name"],
        "power": move_power(pokemon_content["moves"][moves[3]]["move"]["url"]),
        "accuracy": move_accuracy(pokemon_content["moves"][moves[3]]["move"]["url"]),
        "type": move_type(pokemon_content["moves"][moves[3]]["move"]["url"])
    }
    return [move_1, move_2, move_3, move_4]


def attacking_turn(player1, player1_hp, player2_hp):
    ai_available_moves = move_options(ai_pokemon)
    user_available_moves = move_options(user_pokemon)
    if player1 == "ai":
        print("AI to start!")
        game = True
        while game:
            attack_move = random.choice(ai_available_moves)
            print(f"{ai_pokemon.capitalize()} used {attack_move['name']}!")
            hit_chance = random.randint(0, 100)
            if hit_chance > attack_move['accuracy']:
                print("The move misses!")
            else:
                attack_dmg = attack_move['power'] * move_multiplier(attack_move['type'], user_pokemon_info[1])
                print(move_effectiveness(move_multiplier(attack_move['type'], user_pokemon_info[1])))
                player2_hp -= attack_dmg
                print(f"{ai_pokemon} does {attack_dmg} dmg!")
                if player2_hp <= 0:
                    print(f"{user_pokemon} has fainted")
                    game = False
                    continue
                else:
                    print(f"{user_pokemon} is on {player2_hp} hp")
            for index1 in user_available_moves:
                print(
                    f"{user_available_moves.index(index1) + 1}. {user_available_moves[user_available_moves.index(index1)]['name'].capitalize()},       Type: {user_available_moves[user_available_moves.index(index1)]['type'].capitalize()},     Power: {user_available_moves[user_available_moves.index(index1)]['power']},        Accuracy: {user_available_moves[user_available_moves.index(index1)]['accuracy']}")
            user_move_options = [1, 2, 3, 4]
            user_selection = True
            while user_selection:
                user_move = int(input("Please enter a number for the move you wish to select: "))
                if user_move in user_move_options:
                    user_selection = False
                else:
                    print("Error, please try again.")
            attack_move = user_available_moves[int(user_move) - 1]
            print(f"{user_pokemon.capitalize()} used {attack_move['name']}!")
            hit_chance = random.randint(0, 100)
            if hit_chance > attack_move['accuracy']:
                print("The move misses!")
            else:
                attack_dmg = attack_move['power'] * move_multiplier(attack_move['type'], user_pokemon_info[1])
                print(move_effectiveness(move_multiplier(attack_move['type'], user_pokemon_info[1])))
                player1_hp -= attack_dmg
                print(f"{user_pokemon} does {attack_dmg} dmg!")
                if player1_hp <= 0:
                    print(f"{ai_pokemon} has fainted")
                    game = False
                    continue
                else:
                    print(f"{ai_pokemon} is on {player1_hp} hp")
    elif player1 == "user":
        print("User to start!")
        game = True
        while game:
            for index1 in user_available_moves:
                print(
                    f"{user_available_moves.index(index1) + 1}. {user_available_moves[user_available_moves.index(index1)]['name'].capitalize()},       Type: {user_available_moves[user_available_moves.index(index1)]['type'].capitalize()},     Power: {user_available_moves[user_available_moves.index(index1)]['power']},        Accuracy: {user_available_moves[user_available_moves.index(index1)]['accuracy']}")
            user_move_options = [1, 2, 3, 4]
            user_selection = True
            while user_selection:
                user_move = int(input("Please enter a number for the move you wish to select: "))
                if user_move in user_move_options:
                    user_selection = False
                else:
                    print("Error, please try again.")
            attack_move = user_available_moves[int(user_move) - 1]
            print(f"{user_pokemon.capitalize()} used {attack_move['name']}!")
            hit_chance = random.randint(0, 100)
            if hit_chance > attack_move['accuracy']:
                print("The move misses!")
            else:
                attack_dmg = attack_move['power'] * move_multiplier(attack_move['type'], user_pokemon_info[1])
                print(move_effectiveness(move_multiplier(attack_move['type'], user_pokemon_info[1])))
                player2_hp -= attack_dmg
                print(f"{user_pokemon} does {attack_dmg} dmg!")
                if player2_hp <= 0:
                    print(f"{ai_pokemon} has fainted, you win!")
                    game = False
                    continue
                else:
                    print(f"{ai_pokemon} is on {player2_hp} hp")
            attack_move = random.choice(ai_available_moves)
            print(f"{ai_pokemon.capitalize()} used {attack_move['name']}!")
            hit_chance = random.randint(0, 100)
            if hit_chance > attack_move['accuracy']:
                print("The move misses!")
            else:
                attack_dmg = attack_move['power'] * move_multiplier(attack_move['type'], user_pokemon_info[1])
                print(move_effectiveness(move_multiplier(attack_move['type'], user_pokemon_info[1])))
                player1_hp -= attack_dmg
                print(f"{ai_pokemon} does {attack_dmg}!")
                if player1_hp <= 0:
                    print(f"{user_pokemon} has fainted, you lose!")
                    game = False
                    continue
                else:
                    print(f"{user_pokemon} is on {player1_hp}")


def pokemon_sprite(pokemon):  # Broken need fixing
    pokemon_request = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_names.index(pokemon) + 1}")
    pokemon_data = pokemon_request.json()
    sprite_url = pokemon_data["sprites"]["front_default"]

    print(sprite_url)

    image_response = requests.get(sprite_url)
    image = image_response.content
    fp = open(f"{pokemon_names.index(pokemon) + 1}.png", 'wb')
    fp.write(image_response.content)
    fp.close()
    sprite = os.listdir("C:/Users/lukew/PycharmProjects/DevOps_Training/python_fundamentals/examples/day_5")
    img = PIL.Image.open(
        f"C:/Users/lukew/PycharmProjects/DevOps_Training/python_fundamentals/examples/day_5/{pokemon_names.index(pokemon) + 1}.png")

    width, height = img.size
    aspect_ratio = height / width
    new_width = 120
    new_height = aspect_ratio * new_width * (0.55*0.75)
    img = img.resize((new_width, int(new_height)))

    img = img.convert('L')

    # chars = ["T", "⠈", "⣠", "⣿", "⣷", "⣤", "⣶", "⡄", "⡟", "⠉", "⡀"]
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]


    pixels = img.getdata()
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

    sprite_image = open("ascii_image.txt", "r").read()
    sprite_image = sprite_image.replace('@', ' ')
    return sprite_image

    '''
    print(sprite[0])
    img = mpimg.imread('133.png')
    return ascii(sprite[0])
    # plt.imshow(img)
    # plt.show
    # sprite_test = os.startfile(f"C:/Users/lukew/PycharmProjects/DevOps_Training/python_fundamentals/examples/day_5/{pokemon_names.index(pokemon) + 1}.png", 'open')
    # print(f"{pokemon_names.index(pokemon) + 1}.png")
    '''


request_pokemon = requests.get("https://pokeapi.co/api/v2/pokemon-species/?limit=151")
pokemon_content = request_pokemon.json()
# print(pokemon_content)
pokemon_data = pokemon_content["results"]

pokemon_names = []
for index in range(0, 151):
    pokemon_names.append(pokemon_data[index]["name"])
#     print(pokemon_names[index])

# print("Hello traveller, welcome to Sparta Gym, here you will have your chance to get your Global badge!!")
# time.sleep(5)
# print("**Pause for dramatic effect**")
# time.sleep(5)
# print("Found below are the Pokemon from the Kanto Region, please choose your contender")
# time.sleep(5)
# print(f"Pokemon to choose from: {pokemon_names}")
# time.sleep(5)
# print("Enter below the name of the pokemon you wish to choose!")
# time.sleep(1)
# print("Or enter 'random' for a random Pokemon, only do this if you feel lucky!")

user_choosing = True
while user_choosing:
    user_input = input()
    user_pokemon = user_input.lower()
    if user_pokemon in pokemon_names:
        user_choosing = False
    elif user_pokemon == "random":
        user_pokemon = random.choice(pokemon_names)
        user_choosing = False
    else:
        print("Invalid, please choose either a name above or 'random'")

ai_pokemon = random.choice(pokemon_names)

user_pokemon_info = pokemon_stats(user_pokemon)
print(user_pokemon_info)
ai_pokemon_info = pokemon_stats(ai_pokemon)
print(ai_pokemon_info)
time.sleep(1)
print("Welcome to pokemon battle!")
print(f"*user* {user_pokemon} I choose you!")
print("  -----  ")
print(" /     \ ")
print("|       |")
print("|---O---|")
print("|       |")
print(" \     / ")
print("  -----  ")
print(pokemon_sprite(user_pokemon))
time.sleep(1)
print(f"*Ai* {ai_pokemon} I choose you!")
print("  -----  ")
print(" /     \ ")
print("|       |")
print("|---O---|")
print("|       |")
print(" \     / ")
print("  -----  ")
print(pokemon_sprite(ai_pokemon))

# Deciding who starts first
start_turn = move_order(user_pokemon_info[5], ai_pokemon_info[5])

if start_turn == "user_first":
    first_pokemon_info = user_pokemon_info
    first_pokemon = user_pokemon
    player1 = "user"

    second_pokemon_info = ai_pokemon_info
    second_pokemon = ai_pokemon
    player2 = "ai"

elif start_turn == "ai_first":
    first_pokemon_info = ai_pokemon_info
    first_pokemon = ai_pokemon
    player1 = "ai"

    second_pokemon_info = user_pokemon_info
    second_pokemon = user_pokemon
    player2 = "user"

player1_hp = round(first_pokemon_info[2] * (1 + (first_pokemon_info[4] / 600)) * 10)  # Round to whole number
print(f"{first_pokemon}'s hp: {player1_hp}")
player2_hp = round(second_pokemon_info[2] * (1 + (second_pokemon_info[4] / 600)) * 10)
print(f"{second_pokemon}'s hp: {player2_hp}")

attacking_turn(player1, player1_hp, player2_hp)
