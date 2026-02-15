
# This module contains helper functions for validating user details such as name, email, and password.

# this function checks if the name is a string and has more than 2 characters
def validate_name(name):
    if len(name)>2 and type(name)==str:
        return True
    else:
        return False
    
# this function checks if the email contains only one '@' symbol, has a valid username and domain, and ends with a valid top-level domain
def validate_email(email):
    if email.count('@')>1:
        return False
    if '@' in email :
        mail_parts = email.split('@')
        if len(mail_parts[0])>1 and (mail_parts[1].split('.')[-1]) in ['org', 'net', 'edu', 'ac', 'uk', 'com']:
            return True
        return False
    return False

# this function checks if the password is at least 8 characters long, contains at least one uppercase letter, and contains at least one digit
def validate_password(password):
    if len(password)<8:
        return False
    elif not any(char.isupper() for char in password):
        return False
    elif not any(char.isdigit() for char in password):
        return False
    else:
        return True
    
    
