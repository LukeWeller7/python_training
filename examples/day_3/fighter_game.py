import random
import time


def end_conditions(user_index, ai_index):

    if user_index + 2 == ai_index or user_index + 4 == ai_index or user_index - 3 == ai_index or user_index - 1 == ai_index:
        return print(f"You Win! {user_choice} beats {ai_choice}")
    elif user_index + 1 == ai_index or user_index + 3 == ai_index or user_index - 4 == ai_index or user_index - 2 == ai_index:
        return print(f"You Lose: {ai_choice} beats {user_choice}")
    elif user_index == ai_index:
        return print(f"Draw: You both picked {user_choice}")
    else:
        return print("Error")


print("Welcome to Rock, Paper, Scissors, Lizard, Spock")

game = True
while game:
    print("Please choose a number from the options below:")
    options = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    number_list = []

    for i in options:
        print(f"{options.index(i) + 1}. {i}")
        time.sleep(0.5)
        number_list.append(options.index(i) + 1)


    user_choosing = True
    while user_choosing:
        user_input = int(input("Your chosen number: "))
        if user_input in number_list:
            user_choice = options[user_input - 1]
            user_choosing = False
            break
        else:
            print("Invalid option, please try again")
            user_choosing = True

    ai_choice = random.choice(options)
    print(f"you choose: {user_choice}")
    print(f"ai choose: {ai_choice}")

    end_conditions(user_input, options.index(ai_choice) + 1)

    play_again = input("Would you like to play again? (Y/N): ")
    if play_again == "Y":
        game = True
    elif play_again == "N":
        game = False
    else:
        print("An Error has occurred!")
        game = False


