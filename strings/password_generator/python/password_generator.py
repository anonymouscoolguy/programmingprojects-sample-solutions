import string
import random

def main():
    print("Welcome to your favourite password manager.")
    print("Quickly select the desired settings to generate your password.")
    wants_uppercase, wants_lowercase, wants_numbers, wants_special, length = get_setup_settings()

    characters_wanted = create_character_set(wants_uppercase, wants_lowercase, wants_numbers, wants_special)
    if (len(characters_wanted) == 0):
        print("You must select at least on type of characters.")
        return

    generated_password = generate_password(characters_wanted, length)
    print(f"The generated password: {generated_password}")

def get_setup_settings():
    # Uppercase characters
    uppercase_response = get_yes_no_response("Would you like to include uppercase characters? (y/n): ")

    # Lowercase characters
    lowercase_response = get_yes_no_response("Would you like to include lowercase characters? (y/n): ")

    # Numbers
    numbers_response = get_yes_no_response("Would you like to include numbers? (y/n): ")

    # Special characters
    special_response = get_yes_no_response("Would you like to include special characters? (y/n): ")

    # Length
    length_response = get_length_response("What length would you like the password to be? ")

    return [uppercase_response, lowercase_response, numbers_response, special_response, length_response]

def get_yes_no_response(query):
    while True:
        response = input(query)
        response = response.strip().lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("The response must be 'y' or 'n'. Please try again:")

def get_length_response(query):
    while True:
        response = input(query)
        try:
            length = int(response.strip())
            if length > 0:
                return length
            else:
                print("Invalid input. Length cannot be less than 1. Please try again: ")
        except ValueError:
            print("Invalid input. Response must be an integer. Please try again:")
    
def create_character_set(wants_uppercase, wants_lowercase, wants_numbers, wants_special):
    character_set = ""

    if wants_uppercase:
        character_set += string.ascii_uppercase
    
    if wants_lowercase:
        character_set += string.ascii_lowercase

    if wants_numbers:
        character_set += string.digits
    
    if wants_special:
        character_set += string.punctuation
    
    return character_set

def generate_password(character_set, length):
    generated_password = ""
    for _ in range(length):
        generated_password += random.choice(character_set)
    return generated_password

main()