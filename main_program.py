from helper_functions import validate_input, create_message, convert_to_binary
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message

def get_user_info():
    while True:
        name = input("Enter yor name: ")
        age = input("Enter your age: ")
        if not validate_input(name):
            print("Invalid input: Please enter a correct name")
            continue
        if not age.isdigit():
            print("Invalid age. Please anter a valid age")
            continue
    return name, age

if __name__ =='__main__':
    show_intro()
    name, age = get_user_info()
    name_binary, age_binary = convert_to_binary()
    message = create_message()
    save_message()
    read_message()
    show_exit_message()
    
