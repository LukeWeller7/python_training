# Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).


list_of_numbers = list(range(1500, 2701))

suitable_numbers = []
for test in list_of_numbers:
    if (test % 7) == 0 and (test % 5) == 0:
        suitable_numbers.append(test)

# print(f"Numbers that are divisible by 7 and multiples of 5, between 1500 and 2700: {suitable_numbers}")


'''
Write a Python program to construct the following pattern, using a nested loop number.
Expected Output:

1
22
333
4444
55555
666666
7777777
88888888
999999999
'''

for i in range(0, 10):
    print(str(i) * i)

