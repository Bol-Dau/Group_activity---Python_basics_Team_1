#!/usr/bin/python3
#Check whether the user input is a string and whether is empty
def validate_input(user_input):
    if not isinstance(user_input, str):
        return False
    elif not user_input.strip():
        return False
    return True

def convert_to_binary(text):
    text = input("Enter your age: ")
    if text.isdigit():
        age_binary = bin(int(text))
        print(age_binary)
    else:
        for char in text:
            char = ord(char)
            name_binary = format(char,'08b')
            print(name_binary, end=' ')

def create_message(name, age, name_binary, age_binary):
    #Combines all details into a full personalized message.
    message = (f"""
        Hello {name}, you are {age} years old!\n"
        Name in binary: {name_binary}\n"
        Age in binary: {age_binary}"
    """)
    return message
