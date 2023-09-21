# Libraries and Modules

# Pytho has very extensive libraries and modules, this is great for us as DevOps engineers!

# Module = Single file of functions, classes, variables etc. That you can bring in and use in another Python file

# Library = Collection of modules. Needs to be installed with pip

import math
import random
import requests

#
# s = math.sqrt(4)
# print(s)
#
#
# num_float = 23.66
#
# one_third = 1/3
#
# print(math.floor(num_float))
# print(math.floor(1))
# print(math.floor(one_third * 3))


# random_number = random.randint(1, 10)
# print(random_number)

# request_bbc = requests.get("https://www.bbc.co.uk/") # Gets information from given website
#
# print(request_bbc.status_code)
# print(request_bbc.content)
#
# bbc_content = request_bbc.content


request_poke = requests.get("https://pokeapi.co/api/v2/pokemon-species/?limit=151")
poke_content = request_poke.content.split()
poke_data = request_poke.json()
data = poke_data["results"]
print(request_poke)
print(poke_content)

random_poke = random.choice(data)
pokemon_name = random_poke["name"]

print(pokemon_name)

print(request_poke.status_code)
# print(request_poke.content)
