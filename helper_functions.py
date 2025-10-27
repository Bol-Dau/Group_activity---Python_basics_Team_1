#Here we validate the user's input by handling the spaces between names if the user inputs more than one name and we delete trailing spaces
def validate_input(user_input):
    user_input = user_input.strip()
    if user_input and user_input.replace(" ","").isalpha():
        return True
    else:
        return False


 #Here we are going to convert the numbers first into binary then text after because if we deal with text numbers might be wrongly handled as is they are strings
#by using 08b we insure consistency and clarity ensuring that we print 8digits for each letter's binary this is the ASCII value
def convert_to_binary(text):
    if text.isdigit():  
        return bin(int(text))
    else:
        return " ".join(format(ord(char), '08b') for char in text)



