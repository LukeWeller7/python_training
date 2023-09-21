# Collections can stpre multiple pieces of data inside

# Lists - called arrays in other languages

shopping_list = ["milk", "sugar", "potatoes"]
shopping_list.append("eggs")  # Adds one item to the end of the list
shopping_list.extend(["bread", "water"])  # Adds mutliple items to end of the list

# shopping_list.remove("sugar")
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

print(student_1)

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
