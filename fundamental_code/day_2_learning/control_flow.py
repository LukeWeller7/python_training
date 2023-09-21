# Control Flow - Control the flow of your code (make decisions and ignore certain code dependent on factors)

# Check if conditions are true before you run a piece of code. Can think of each control flow statement as a boolean.

# if, elif, else

# if

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

# In Python there are no switch statements or case statements. Python is nice and simple
