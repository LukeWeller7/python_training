print("Username and Password Storage") # User welcome


# This sections creates the inital storage system for username and passwords
password_Manager = {
    "lweller": "Password123",
    "jsmith": "Sparta492",
    "ljohnson": "BS1997BBW",
    "jderulo": "JasonDerulo",
    "jdoe": "ILoveAmerica"
}   # This is the original dictionary with the inital usernames and passwords
# print(password_Manager) # Test print



tasks = ["1.Retrieve your password", "2.Changing your password", "3.New User", "4.Other"]
for a in range(len(tasks)):
    print(tasks[a])
user_task_request = int(input("Please select the number on the service you wish to use: "))



# Section on the ability to retrieve a password via inputted user name
if user_task_request == 1:
    retrieve_password = input("You have selected retrieve a password, is this correct? (Y/N): ") # Asking the user whether they want to retrieve their password

    if retrieve_password == "Y": # If the user selected Y (yes) then they complete this section of the code
        username = input("Please enter your username: ") # User inputs theirs username
        if username in password_Manager: # Check if their username is in the system
            print(password_Manager.get(username)) # Printing out the password associated with given username
        else:
            print("I'm sorry, that username is not found in our system.") # If username not in system, this message will occur




#Section on the ability for the user to change their current password, including a part where the user has to provide a their password
if user_task_request == 2:
    change_password = input("You have selected change password, is this correct? (Y/N): ") # Asking the user whether they want to change their password

    if change_password == "Y": # If the user selected Y (yes) then they complete this section of the code
        username = input("Please enter your username: ") # Confirm the User's username
        old_password = input("Please enter your old password: ") # User inputs their old password
        if old_password == password_Manager.get(username): # Ensuring this password match the password in our system
            new_password = input("Please now enter your new password: ") # Prompt to enter new password
            password_Manager[username] = new_password # Change password in system to new one
        else:
            print("Incorrect username or password!") # Telling the User that the password doesn't match the username


# print(password_Manager) # Test print




# Section where a new user can add their username and password to the system.
if user_task_request == 3:
    new_user = input("You have selected new user, is this correct? (Y/N): ") # Asking the user whether they are a new user
    i = 0
    if new_user == "Y": # If the user selected Y (yes) then they complete this section of the code
        while i != 1: # This sets up a while loop that will continue until i reaches 1
            username = input("Please enter your username: ") # User inputs a username
            if username in password_Manager: # Check to see if it's unique or not
                print("This username is already Taken.") # Username already in use
                i = 0 # i stays at zero to keep while loop going allowing user to re-enter a new username
            else: # If the username is unique to our system
                i = 1 # Sets i to 1 so the while loop ends
        password = input("Please enter your password: ") # Allow user to add a password

        password_Manager[username] = password # Adding both the new username and password to the dictionary


if user_task_request == 4:
    print("For addition services and help, please call 44455566677")


print("Thank you for using our services today!")
print(password_Manager) # Test print




# Notes and suggestions to improve the system:
#   - DONE!!!  Start of the code, creating a section that helps navigate the user to the write section, so they don't have to go through all three stages each time.
#       - Option to restart the process for extra services
#       - If user presses wrong number, take them back to start
#   - New user, when the user enters a username that's already taken, provide suggestions for unused usernames.
#   - Add some sort of security question that's required for the user to answer before retrieving their password.
