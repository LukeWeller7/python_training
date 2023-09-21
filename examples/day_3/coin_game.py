import random


random_choice = random.randint(0, 1)


if random_choice == 0:
    print("Heads!")
elif random_choice == 1:
    print("Tails!")
else:
    print("Error!")
