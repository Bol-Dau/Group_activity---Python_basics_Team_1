#!/usr/bin/python3
# We began by importing create_message function from helper_functions.py to use it while saving and reading messages.
from helper_functions import create_message

# We then defien a file name where the user message will be stored when saved, and also accessed when reading the message.
user_message_file="user_message.txt"

# We then deifene the first function that will help in saving the message to a file.
def save_message(message):
    with open(user_message_file, "a") as file: # Open the file in append mode such that we can add new messages without overwriting the existing ones.
        file.write(message)
    print("Message saved to user_message.txt ") # Notify the user that the messaage has successfully been saved.

# We then define the second function that will help in reading the saved message from the file.
def read_message():
    # We use try and except block to handle errors gracefully while trying to read the file.
    try:
        with open(user_message_file, "r") as file: # Open the file in read mode to access the saved message.
            message = file.read()
            print("Saved message:\n", message)
    
    except FileNotFoundError: # This will catch the error if the file is not found
        print("Error: The file 'user_message.txt' was not found.")
    
    except Exception as e: # This will catch any other general errors that may occur
        print("An error occurred:", e)
