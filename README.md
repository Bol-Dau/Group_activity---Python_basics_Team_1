# Group_activity---Python_basics_Team_1

This Python program collects a user's name and age, converts them to binary, creates a personalized message, and saves/reads it from a text file. It also handles input and file errors gracefully.

Project Structure

1. helper_functions.py

validate_input(user_input): Checks if input is a non-empty string. Returns True or False.

convert_to_binary(text): Converts a name to ASCII binary (e.g., "Hi" → "01001000 01101001") or converts age to binary using bin().

create_message(name, age, name_binary, age_binary): Builds a message including the name, age, and their binary representations.

2. file_manager.py

save_message(message): Saves the message to user_message.txt and prints confirmation.

read_message(): Reads and prints the saved message, using try/except for error handling.

3. greetings.py

show_intro(): Displays a friendly welcome message.

show_exit_message(): Displays a goodbye message.

4. main_program.py

Controls program flow by importing all other functions.

get_user_info(): Collects and validates user name and age in a loop.

Main block: Calls the intro, collects input, converts to binary, creates and saves the message, reads it back, and shows exit message.

How to Run

Ensure all four Python files are in the same directory.

Run the program using:

python3 main_program.py


Follow the prompts to enter your name and age.

View the personalized message and its binary representation.
