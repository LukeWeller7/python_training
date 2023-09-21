

user_number  = int(input("Please insert a number: "))

odd_even_checker = user_number % 2

if odd_even_checker == 0:
    print("Your number is Even")
elif odd_even_checker == 1:
    print("Your number is odd")
else:
    print("An ERROR has occurred!")
