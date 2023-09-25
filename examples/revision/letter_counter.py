user_sentence = input()
user_letter = input("Select the letter you want to count: ")

def letter_counter(letter):
    counter = user_sentence.count(letter)
    return counter

print(letter_counter(user_letter))
