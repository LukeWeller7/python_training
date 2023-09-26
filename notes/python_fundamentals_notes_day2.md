# Control Flow 
### Control the flow of your code (make decisions and ignore certain code dependent on factors)
Check if conditions are true before you run a piece of code. Can think of each control flow statement as a boolean.

if, elif, else

# Code example:
```python
age = 19 # Can replace with user input

if age >= 18:
    print("You are able to see all films that are available")

elif age >= 15:
    print("You are od enough to watch all films that are PG, 12, and 15")
elif age >= 12:
    print("You are old enough to watch films rated 12, and PG")
else:
    print("You are able to watch PG movies")


film_rating = "U"

if film_rating.lower() == "u":
    print("All age groups can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidence is advised for this movie")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("People aged 12 or over can watch this film unsupervised. Younder people must be supervised.")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie.")
elif film_rating.lower() == "18":
    print("People aged 18 or over can watch this movie")
# else - Way to round off control flow block, also good tester to see if error occurs.
else:
    print("This is not a valid rating, please use 'u', 'pg', '12' or '12a', '15', '18'.")
```

In Python there are no switch statements or case statements. Python is nice and simple



# For Loops
For each loops (other languages) for each item in a list, similar to completing for i in range len(variable)

Python uses 'for' only, no 'for each' loops

```python
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]

for num in list_data:
    print(num * 2)


for num in embedded_lists:
    for g in num:
        print(g * 2)

```
# Looping through dictionaries
```python
dict_data = {
    1: {"name": "Bronson",
        "money": "£0.05"},
    2: {"name": "Jack",
        "money": "£3.98"},
    3: {"name": "John",
        "money": "£10.23"}
}
print(dict_data)

for item in dict_data.values():
    print(item)
    for data in item.values():
        print(data)


# get values for individual keys
for items in dict_data.values():
    print(items["money"])
```

# Loops and if statements
```python
list_data = [1, 2, 3, 4, 5]
for num in list_data:
    if num % 2 == 0:
        print(f"{num}, is even!")
    elif num % 2 == 1:
        print(f"{num} is odd!")
    else:
        print("ERROR")
```
# Diagram Breakdown of While Loops
![](images\While_loop_diagram.png)
# Diagram breakdown of For Loops
![](images\For_loop_diagram.png)
# Diagram breakdown for If, Elif, Else Statements
![](images\If_Statement_Diagram.png)





Snapshots (Conceptual)

Store changes as a base version originally (clunky and didn't allow complexity)

Git takes a picture of your code at certain time and saving that not the base file, saves referneces to most recent version of the file.

dont need to go online with git, it's localised, all versions work locally. This makes git fast. You dont need to necessarily links up to a cloud net. Because of that difference

Don't have to involve github and online repos.

# The three states


Important when getting to more complex and larger work

modified, staged, and committed

modified, not telling git you have changed a file
staged, telling git you have changed something, git knows what's changed, but not saved
committed, safely store the data within git

files are always inside of one of these three stages

working directory, staging area, commit
