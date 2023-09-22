import os


user_path = input("Enter the path of the directory you desire: ")
user_filename = input(" Enter the desired file name: ")

os.makedirs(user_path)
file_path = os.path.join(user_path, user_filename)
open(file_path, 'w').close()
