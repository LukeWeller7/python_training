def addition(add1, add2):
    return add1 + add2


def subtraction(sub1, sub2):
    return sub1 - sub2


def multiply(multi1, multi2):
    return multi1 * multi2


def division(div1, div2):
    return div1 / div2

print("Enter below two numbers: ")
user_input1 = int(input())
user_input2 = int(input())
print(f"addition {addition(user_input1,user_input2)}")
print(f"subtraction {subtraction(user_input1,user_input2)}")
print(f"multiplied {multiply(user_input1,user_input2)}")
print(f"divided {division(user_input1,user_input2)}")
