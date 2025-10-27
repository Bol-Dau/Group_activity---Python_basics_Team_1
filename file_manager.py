#!/usr/bin/python3
def save_message():
    user_message = input("Enter a message to save: ")
    with open("user_message.txt", "w") as file:
        file.write(user_message)
    print("Message saved to user_message.txt ")

def read_message():
    try:
        with open("user_message.txt", "r") as file:
            message = file.read()
            print("Saved message:", message)
    
    except FileNotFoundError:
        print("Error: The file 'user_message.txt' was not found.")
    
    except Exception as e:
        print("An error occurred:", e)
