def addition(add1, add2):
    return add1 + add2


def subtraction(sub1, sub2):
    return sub1 - sub2


def multiply(multi1, multi2):
    return multi1 * multi2


def division(div1, div2):
    return div1 / div2


print("Calculator: Please enter below the first number you'd like to use: ")
user_number1 = int(input())


break_out = False
i = 0
while i !=2:
    if i == 1:
        print("Would you like to continue? Yes(1), No(2): ")
        yes_no = int(input())
        if yes_no == 2:
            break_out = True
            print(f"Your answer is: {user_number1}")
            break
    if break_out:
        break
    print("Please choose what operation you want to use (addition, subtraction, multiply, division): ")
    user_function = input()
    print(f"Enter below the number you'd like to {user_function}")
    user_number2 = int(input())
    if user_function == "addition":
        user_number1 = addition(user_number1, user_number2)
    elif user_function == "subtraction":
        user_number1 = subtraction(user_number1, user_number2)
    elif user_function == "multiply":
        user_number1 = multiply(user_number1, user_number2)
    elif user_function == "division":
        user_number1 = division(user_number1, user_number2)
    print(user_number1)
    i =1
