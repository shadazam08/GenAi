# Task 3: Custom Exception: Age Validator

# check age valid or not function
def check_age(age):
    # Check if age is outside the valid range (1 to 120)
    if age < 1 or age > 120:
        raise ValueError("Age must be between  1 and 120")
    
# main code
try:
    # take age input from user
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except ValueError as ve:
    print(f"{ve}")
else:
    print("Age is valid")
finally:
    print("Age validation completed.")