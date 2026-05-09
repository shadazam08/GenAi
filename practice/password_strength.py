def password_strength(password):
    if len(password) < 8:
        print(f"the enter password '{password}' is a week password because it is less than 8 Characters.")
    elif not any(char.islower() for char in password):
        print(f"the enter password '{password}' is a week password because it does not contain any lowercase letters.")
    elif not any(char.isupper() for char in password):
        print(f"the enter password '{password}' is a week password because it does not contain any uppercase letters.")
    elif not any(char.isdigit() for char in password):
        print(f"the enter password '{password}' is a week password because it does not contain any digits.")
    elif not any(char in "!@#$^&()%*+-=?" for char in password):
        print(f"the enter password '{password}' is a week password because it does not contain any special characters.")
    else:
        print(f"the enter password '{password}' is a strong password.")

# Example usage
inputPassword = input("Enter a password: ")
password_strength(inputPassword)
