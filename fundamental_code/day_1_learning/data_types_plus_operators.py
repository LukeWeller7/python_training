# What are operators?

# Symbols that execute a particular mathematical or logical function.

# Arithemtic operators:
# +, -, *, /, %

# Logical (Comparison) operators:
# >, <, ==, !=, <=, >=

# Numeric types
# integer, float, complex

a = 45.0
b = "Hello World said:'Hello World'"

print(b[6:])
print(b[:5])
print((len(b.strip('a'))))


c = "32"

print(float(c))

# f-strings

name = "Luke"
age = 22
height_cm = 183.4

print(f"{name} is {age} years old and {height_cm}cm tall")

snoop = "Snoopy"
snoop_years = 63

print(f"{snoop.upper()} IS {snoop_years * 7} YEARS OLD IN DOG YEARS!")

# Rounding
pi = 3.14159265359

print(pi.__round__(3))
print(f"Pi to 3 decimal places: {pi:.3f}")

# Percentage

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}") # % is not modular but places it as a percentage
    # f-strings are useful for general display for user understandance, but for my logical approach thats when youll start with round
print(f"You scored {score/max_score:.0%}") # .2 determines the number of decimal places



