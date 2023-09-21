user_test = True

while user_test:
    user_number = input("Please enter a number! ")
    if user_number.isdigit():
        user_test = False
    else:
        print("Please use digits only")

number = int(user_number)

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz!")
elif number % 5 == 0:
    print("Buzz!")
elif number % 3 == 0:
    print("Fizz!")
else:
    print("Nothing to see here!")


