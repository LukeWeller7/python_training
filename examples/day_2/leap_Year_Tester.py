user_input = int(input("Please insert a year: "))

test_year = user_input

if (test_year % 4) == 0:
    if (test_year % 100) == 0:
        if (test_year % 400) == 0:
            print("This year is a leap year!")
        else:
            print("This year is not a leap year!")
    else:
        print("This year is a leap year!")
else:
    print("This year is not a leap year!")




