#!/usr/bin/python3
from helper_functions import create_message
user_message_file="user_message.txt"
def save_message(message):
    with open(user_message_file, "a") as file:
        file.write(message)
    print("Message saved to user_message.txt ")

def read_message():
    try:
        with open(user_message_file, "r") as file:
            message = file.read()
            print("Saved message:\n", message)
    
    except FileNotFoundError:
        print("Error: The file 'user_message.txt' was not found.")
    
    except Exception as e:
        print("An error occurred:", e)
