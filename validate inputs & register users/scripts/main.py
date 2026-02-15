# This is the main module for validating and registering a user. It imports helper functions from the hepler_fuctions module to validate the user's name, email, and password.
from hepler_fuctions import *

# This function validates the user's name, email, and password using the helper functions. If any of the details are invalid, it raises a ValueError with an appropriate message. If all details are valid, it returns True.
def validata_user(name,email,password):
    if not validate_name(name):
        raise ValueError('invalid name')
    elif not validate_email(email):
        raise ValueError('invalid email')
    elif not validate_password(password):
        raise ValueError('invalid password')
    else:
        return True
    

# This function registers a user by first validating the user's details using the validata_user function. If the details are valid, it creates a dictionary with the user's name, email, and password and returns it. If any of the details are invalid, it raises a ValueError with an appropriate message.
def register_user(name,email,password):
    try:
        validata_user(name,email,password)

        user_details = {
            'name':name,
            'email':email,
            'password':password
        }
        return user_details

    except ValueError :
        raise ValueError('invalid user details')
    

# This block of code prompts the user to enter their name, email, and password, and then calls the register_user function with the provided details. If the registration is successful, it prints the user's details. If any of the details are invalid, it raises a ValueError with an appropriate message.
name = input('Enter your name: ')
email = input('Enter your email: ')
password = input('Enter your password: ')

result = register_user(name,email,password)

print(result)
