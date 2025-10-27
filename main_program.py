#!/usr/bin/python3
# We begin by importing necessary functions from other files that we will use in this main program.
from helper_functions import validate_input, create_message, convert_to_binary
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

# Then define a function to get user information and validate it.
def get_user_info():
    while True:
        name = input("Enter yor name: ") # Ask the user for their name
        if validate_input(name) == True and not name.isdigit() and name.isalpha(): # Validating to make sure that it's not empty and contains only letters.
            break
        else:
            print("Invalid input: Please enter a correct name") # Print an Error message for invalid input and then continue untill a valid name is provided.
            continue

    while True:
        age = input("Enter your age: ") # Ask the user for their age
        if not age.isdigit(): # Validating to make sure that it only contains digits.
            print("Invalid age. Please enter a valid age") # Print an Error message for invalid input and then continue untill a valid age is provided.
            continue
        else:
            break
    return name, age

if __name__ =='__main__': # This block will only run if this file is executed directly, not when imported as a module.
    show_intro() # This will display a welcome message to the user.
    name, age = get_user_info() # This will get the user's name and age after validation.
    name_binary=convert_to_binary(name) # This will convert the user's name to binary format.
    age_binary=convert_to_binary(age) # This will convert the user's age to binary format.
    create_message(name, age, name_binary=any, age_binary=any) # This will create a personalized message using the user's details.
    save_message(message=str(create_message(name, age, name_binary, age_binary))) # This will save the personalized message to a file.
    read_message() # This will read and display the saved message from the file.
    show_exit_message() # This will display a goodbye message to the user.
