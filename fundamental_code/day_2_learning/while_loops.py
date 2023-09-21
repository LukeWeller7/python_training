# While loops

# For loops are all to do with iterating through a collection
# While loops are more like a monitor -> while something is true, then act.


# x = 1
#
# while x < 11:
#     print(f"It's working --> {x}")
#     if x == 4:
#         break # breaks out of the while loop
#     x += 1


# verifying user input
user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit():
        if int(age) >= 0 and int(age) <= 120:
            user_prompt = False
        else:
            print("Please enter a reasonable number.")
    else:
        print("Please enter your age in digits.")

print(f"Your age is {age}")
