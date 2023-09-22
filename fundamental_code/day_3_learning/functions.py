# Functions

# DRY - Don't Repeat Yourself

# Allows us to embed/reference code, making it reusable.

# Making a function

# def print_something(print_string):
#     print(f"Something has been printed: {print_string}")
#
#
# print_something(1)
# print_something("We can print here")
# print_something(f"hello Luke")


def greeting(name):
    return print(f"Hello, my name is {name}")

greeting("Luke")


# The return statement

# def addition(int1, int2):
#     return int1 + int2
#
#
# addition(2, 1)
# print(addition(2, 2))


# def addition(int1=2, int2=4): # Default functions so that unless new arguments are provided then the default ones are used
#     return int1 + int2
#
#
# addition(2, 1)
# print(addition(2, 2))
# print(addition())


# multiple arguments

# def multi_args(arg2, *multiagrs):  # * stands for wild card, have as many arguments you want.
#     for arg in multiagrs:
#         print(arg)
#     print(arg2)
#     print(type(multiagrs))  # tuple
#
#
# multi_args(1, 2, 3, 4, 5, 6)


# Type hints - can research this


# Functions good practices

# Add useful comments to explain your functions!
# Clear function names and arguments names
# Keep your functions small and compact
# Avoid duplication
# Correct indentation and formatting/syntax
# Organised properly
# Do not use functions unnecessarily
# Functions at the start of your code if possible
# Always return the statement!
# Consider using type hints
