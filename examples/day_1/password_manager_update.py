import time

print("Username and Password Storage")  # User welcome

# This sections creates the initial storage system for username and passwords
password_Manager = {
    "lweller": "Password123",
    "jsmith": "Sparta492",
    "ljohnson": "BS1997BBW",
    "jderulo": "JasonDerulo",
    "jdoe": "ILoveAmerica"
}  # This is the original dictionary with the inital usernames and passwords
# print(password_Manager) # Test print


t = 0
while t != 1:
    tasks = ["1.Retrieve your password", "2.Changing your password", "3.New User", "4.Other", "5.End Call"]
    for a in tasks:
        time.sleep(0.5)
        print(a)
    user_task_request = int(input("Please select the number on the service you wish to use: "))
    requests = [1, 2, 3, 4, 5]

    if user_task_request in requests:
        t = 1
        # Section on the ability to retrieve a password via inputted user name
        if user_task_request == 1:
            retrieve_password = input("You have selected retrieve a password, is this correct? (Y/N): ")  # Asking the user whether they want to retrieve their password

            if retrieve_password == "Y":  # If the user selected Y (yes) then they complete this section of the code
                username = input("Please enter your username: ")  # User inputs theirs username
                if username in password_Manager:  # Check if their username is in the system
                    print(password_Manager.get(username))  # Printing out the password associated with given username
                else:
                    print("I'm sorry, that username is not found in our system.")  # If username not in system, this message will occur
            else:
                print("We were unable to continue with your request, please select the correct number for the service you require.")
                t = 0

        # Section on the ability for the user to change their current password, including a part where the user has to provide a their password
        if user_task_request == 2:
            change_password = input("You have selected change password, is this correct? (Y/N): ")  # Asking the user whether they want to change their password

            if change_password == "Y":  # If the user selected Y (yes) then they complete this section of the code
                j = 0
                incorrect_guesses = 0
                while j != 1:
                    username = input("Please enter your username: ")  # Confirm the User's username
                    old_password = input("Please enter your old password: ")  # User inputs their old password
                    if old_password == password_Manager.get(username):  # Ensuring this password match the password in our system
                        new_password = input("Please now enter your new password: ")  # Prompt to enter new password
                        password_Manager[username] = new_password  # Change password in system to new one
                        j = 1
                    else:
                        print("Incorrect username or password!")# Telling the User that the password doesn't match the username
                        j = 0
                        incorrect_guesses += 1 # This tracks the amount of incorrect guesses the user has used

                    if incorrect_guesses == 3:
                        j = 1
                        print("You have reached the max amount of guesses, please try again later.")
            else:
                print("We were unable to continue with your request, please select the correct number for the service you require.")
                t = 0

        # print(password_Manager) # Test print

        # Section where a new user can add their username and password to the system.
        if user_task_request == 3:
            new_user = input("You have selected new user, is this correct? (Y/N): ")  # Asking the user whether they are a new user
            i = 0
            if new_user == "Y":  # If the user selected Y (yes) then they complete this section of the code
                while i != 1:  # This sets up a while loop that will continue until i reaches 1
                    username = input("Please enter your username: ")  # User inputs a username
                    if username in password_Manager:  # Check to see if it's unique or not
                        print("This username is already Taken.")  # Username already in use
                        i = 0  # i stays at zero to keep while loop going allowing user to re-enter a new username
                    else:  # If the username is unique to our system
                        i = 1  # Sets i to 1 so the while loop ends
                password = input("Please enter your password: ")  # Allow user to add a password

                password_Manager[username] = password  # Adding both the new username and password to the dictionary
            else:
                print("We were unable to continue with your request, please select the correct number for the service you require.")
                t = 0

        if user_task_request == 4:
            print("For addition services and help, please call 44455566677")

        if user_task_request == 5:
            break
    else:
        print("The number you entered is invalid, please try again. Please enter either 1, 2, 3, or 4 below.")
        time.sleep(1)
        t = 0

print("Thank you for using our services today!")
# print(password_Manager)  # Test print

# Notes and suggestions to improve the system:
#   - DONE!!!  Start of the code, creating a section that helps navigate the user to the write section, so they don't have to go through all three stages each time.
#       - Option to restart the process for extra services
#       - DONE!!! If user presses wrong number, take them back to start
#   - New user, when the user enters a username that's already taken, provide suggestions for unused usernames.
#   - Add some sort of security question that's required for the user to answer before retrieving their password.


# User Stories and acceptance criteria
# As a user, I want an end call option, so that I can end the call if I require no help.
#       - Given I am in the service selection, when I choose option to end call, Then I should see that the call has disconnected.
#       - Given I am in the service section, When I choose the option to end call, Then I should see a thank you message signifying the call has ended.
#           - (Need to add extra service option that immediately ends the code
#            - Include a thank you message
# As a user, I want addition options, so that I do have to restart the process if I require multiple services
#       - Given I am completing a provided service, When I finish the service, Then I should see an option for any additional services
#           - Add additional input and for loop asking the user for additional services
# As the admin, I want a security question, so that the service can provide additional protection.
#       - Given I am retrieving my old password, When I enter my username, Then I should be asked a security question to confirm my identity
#           - Need to create a dictionary for each username that includes both password and security answer
# As a user, I want new username suggestions, so that I can easily choose a new username that's available
#       - Given I am creating a new user, When I enter a username that's already take, Then I should be offered a suggestion for a similar username that's not already taken
#           - Need to take the user input and add to the end a random number (randomly generated)
#           - Create a while loop that checks the system to see if the suggested username is unique or not, if so suggest to user, if not regenerate until unique is found.
