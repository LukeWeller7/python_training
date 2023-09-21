# Functions

DRY - Don't Repeat Yourself

Allows us to embed/reference code, making it reusable.

Making a function
```python
def print_something(print_string):
    print(f"Something has been printed: {print_string}")


print_something(1)
print_something("We can print here")
print_something(f"hello Luke")


def greeting(name):
    return print(f"Hello, my name is {name}")

greeting("Luke")


# The return statement

def addition(int1, int2):
    return int1 + int2


addition(2, 1)
print(addition(2, 2))


def addition(int1=2, int2=4): # Default functions so that unless new arguments are provided then the default ones are used
    return int1 + int2


addition(2, 1)
print(addition(2, 2))
print(addition())


# multiple arguments

def multi_args(arg2, *multiagrs):  # * stands for wild card, have as many arguments you want.
    for arg in multiagrs:
        print(arg)
    print(arg2)
    print(type(multiagrs))  # tuple


multi_args(1, 2, 3, 4, 5, 6)
```
Type hints - can research this


### Functions good practices

- Add useful comments to explain your functions!  
- Clear function names and arguments names  
- Keep your functions small and compact  
- Avoid duplication  
- Correct indentation and formatting/syntax  
- Organised properly  
- Do not use functions unnecessarily  
- Functions at the start of your code if possible  
- Always return the statement!  
- Consider using type hints  


# Libraries and Modules
Pytho has very extensive libraries and modules, this is great for us as DevOps engineers!

Module = Single file of functions, classes, variables etc. That you can bring in and use in another Python file

Library = Collection of modules. Needs to be installed with pip
```python
import math
import random
import requests


s = math.sqrt(4)
print(s)


num_float = 23.66

one_third = 1/3

print(math.floor(num_float))
print(math.floor(1))
print(math.floor(one_third * 3))


random_number = random.randint(1, 10)
print(random_number)

request_bbc = requests.get("https://www.bbc.co.uk/") # Gets information from given website

print(request_bbc.status_code)
print(request_bbc.content)

bbc_content = request_bbc.content


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
print(request_poke.content)
```

# Useful Libraries

- Math (contains the fundamental functions of mathematical equations such as sqrt, factorial, pi etc.)
- Random (Provide a system that can generate a random value from a given list or range.)
- Requests (Makes HTTPS requests a lot simpler and faster.)
- PyGames (Designed to provide 2D graphics aimed at gaming developement.)
- Matplotlib (Data visualization, providing graphs.)
