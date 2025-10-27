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
        name_binary = ""  
        # Initialize an empty string to store the binary representation of each character in the name
        for char in text:  
            # Loop through each character in the string (assumes this is the user's name)
            name_binary += format(ord(char), '08b') + " "  
            # Convert the character to its ASCII value using ord()
            # Format the ASCII value as an 8-bit binary string using '08b'
            # Append this binary string to name_binary with a space in between characters
        return name_binary.strip()  
        # Return the final binary string, removing any trailing space at the end


#Creating the Personalized Messag e

def create_message(name, age, name_binary, age_binary):
    #Combines all details into a full personalized message.
    message = f"""
        Hello {name}, you are {age} years old!
        Name in binary: {name_binary}
        Age in binary: {age_binary}
    """
    return message
