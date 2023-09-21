# For Loops

# For each loops (other languages) for each item in a list, similar to completing for i in range len(variable)

# Python uses 'for' only, no 'for each' loops

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {
    1: {"name": "Bronson",
        "money": "£0.05"},
    2: {"name": "Jack",
        "money": "£3.98"},
    3: {"name": "John",
        "money": "£10.23"}
}
# print(dict_data)


# for num in list_data:
#     print(num * 2)


# for num in embedded_lists:
#     for g in num:
#         print(g * 2)


# looping through dictionaries
# for item in dict_data.values():
#     print(item)
#     for data in item.values():
#         print(data)


# get values for individual keys
for items in dict_data.values():
    print(items["money"])


# loops and if statements
for num in list_data:
    if num % 2 == 0:
        print(f"{num}, is even!")
    elif num % 2 == 1:
        print(f"{num} is odd!")
    else:
        print("ERROR")
