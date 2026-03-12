import re  # I use the 're' module for email pattern validation using regular expressions.

def validate_name(prompt):
    '''
    This function checks if the entered name is valid.
    I ensure it is not empty and contains only alphabetic characters and spaces.
    This avoids issues like numbers or symbols in names.
    '''
    while True:
        name = input(prompt).strip()  # Remove leading/trailing spaces
        if not name:
            print("Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")  # Prevent numbers or special characters
        else:
            return name  # Return cleaned and valid name

def validate_non_empty(prompt):
    '''
    A general-purpose validator to ensure input is not empty.
    I use this for fields like subjects where any text is allowed, but it should not be blank.
    '''
    value = input(prompt).strip()
    while not value:
        print("Input cannot be empty.")
        value = input(prompt).strip()
    return value  # Return valid non-empty input

def validate_integer(prompt):
    '''
    This validator ensures the user enters a positive integer (e.g., IDs).
    I use try-except to catch invalid input like letters or symbols.
    '''
    while True:
        try:
            value = int(input(prompt))  # Try to convert input to integer
            if value > 0:
                return value  # Only accept positive numbers
            print("Value must be positive.")
        except ValueError:
            print("Invalid number. Try again.")  # Handle non-integer input

def validate_age(prompt):
    '''
    This function makes sure the entered age is an integer between 4 and 20.
    These values are based on realistic school ages.
    '''
    while True:
        try:
            age = int(input(prompt))
            if 4 <= age <= 20:
                return age  # Accept if within valid age range
            print("Age must be between 4 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle invalid input like text

def validate_email(prompt):
    '''
    This function checks if the entered email address matches a valid format.
    I use a regular expression to ensure it contains @, a domain, and ends properly (e.g. .com, .ru).
    '''
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        email = input(prompt).strip()
        if re.match(email_pattern, email):  # Use regex to validate format
            return email  # Return valid email
        print("Invalid email format. Try again.")  # Ask again if format is wrong

