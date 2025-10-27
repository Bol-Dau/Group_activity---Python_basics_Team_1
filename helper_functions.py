#!/usr/bin/python3

#Validating User Input

#Check whether the user input is a string and whether is empty
def validate_input(user_input):
    if not isinstance(user_input, str): #check whether the input is a string
        return False
    elif not user_input.strip():#Check if the input is empty after stripping of the white space
        return False
    return True


#Binary Conversion

#Here we Converted the name and age to binary numbers
def convert_to_binary(text):
    if text.isdigit(): #Check whether the input is a digit
        age_binary = bin(int(text)) #Convert the age to an integer and then the integer to a binary display
        return age_binary
    else:
        for char in text: #iterating over all characters in the name
            char = ord(char) #converting the characters in the name to ASCII values
            name_binary = format(char,'08b') #Converting the ASCII values to binry using the format function and '08b' to ensure that the binary representation is 8 bits long rather than 7
            name_binary = name_binary =+ " "
            return name_binary


#Creating the Personalized Messag e

def create_message(name, age, name_binary, age_binary):
    #Combines all details into a full personalized message.
    message = (f"""
        Hello {name}, you are {age} years old!\n"
        Name in binary: {name_binary}\n"
        Age in binary: {age_binary}"
    """)
    return message
