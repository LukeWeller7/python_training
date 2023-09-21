# Variables

### What is a variable?
Label data within a program and store it. So it can be referenced later.

Python is dynamically typed language

# Data types plus operators

### What are operators?
Symbols that execute a particular mathematical or logical function.

Arithemtic operators:  
 +, -, *, /, %

Logical (Comparison) operators:  
'>, <, ==, !=, <=, >='

Numeric types:  
integer, float, complex
```python
a = 45.0
b = "Hello World said:'Hello World'"

print(b[6:]) # Prints phrase starting from World
print(b[:5]) # Prints up until 5th index value
print((len(b.strip()))) # Prints the lenght of b as well as removes any spaces at the end of the phrase


c = "32" # Set varibale as a string

print(float(c)) # Prints the variable as a float not string

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

print(pi.__round__(3)) # Rounding to 3 dp
print(f"Pi to 3 decimal places: {pi:.3f}") # Alternative way to round
    
# Percentage
    
score = 16
max_score = 26
    
print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}") # % is not modular but places it as a percentage
print(f"You scored {score/max_score:.0%}") # .2 determines the number of decimal places'

# f-strings are useful for general display for user understandance, but for my logical approach thats when youll start with round
```
# Boolean

### What is a boolean?
Binary option between True or False.

```python
a = True
b = False
   
print(a) # Will print True
   
   
# Boolean methods
   
hi = "55555"
   
print(hi.isnumeric()) # Printing whether hi is made of only numerical values
print(hi.isalpha()) # Printing whether hi is made of only alphabetical values
   
#Boolean values
#When variable is 0 its false, otherwise its true
   
x = 0
y = "no"
   
   
print(bool(x)) # Prints False
print(bool(y) + 1) # Prints 2
   
#Value None, not true, not false (null in other languages)
#Use as a placeholder value
   
z = None
   
print(bool(z)) # Prints False
print(z is None) # Prints True
   
print(type(z)) # Prints class NullType
```
# Collections
Collections can store multiple pieces of data inside
```python
# Lists - called arrays in other languages

shopping_list = ["milk", "sugar", "potatoes"]
shopping_list.append("eggs")  # Adds one item to the end of the list in this case eggs
shopping_list.extend(["bread", "water"])  # Adds mutliple items to end of the list

shopping_list.remove("sugar") # removes particular item stated
# shopping_list.pop() # Removes item based on index value
# shopping_list.remove() # Removes item based on data value
print(shopping_list[0::])  # start, stop, step (negative step counts backwards on list


# Tuples - Immutable, they cannot be changed!

essentials = ("bread", "eggs", "milk")


# What is a dictionary?

# Use key/value pairs
# key = the reference to the object
# value = the data storage mechanism you want to use (variable, list, dictionary etc.)

# Making a Dictionary

student_1 = {
    "name": "Luke Weller",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data types", "operators"]
}

print(student_1) # Printing Dictionary

print(student_1["completed_lesson_names"][0]) # Variables

# Changing a value in a dictionary

student_1["completed_lessons"] = 3

print(student_1["completed_lessons"])

student_1["completed_lesson_names"].remove("data types")

print(student_1)

# Getting the keys

print(student_1.keys())


# Sets and Frozen sets
# Sets provide a list style format that is in a random order and can't have duplicated items
# Frozen set provides the same as a Set however it's immutable, cannot change them.

car_parts = {"wheels", "doors", "exhaust", "seats", "windows"}
print(car_parts)

car_parts.add("wheels")
print(car_parts)
```
