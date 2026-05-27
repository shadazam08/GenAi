def even_to_odd(num):
    if isinstance(num, int):
        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")
    elif isinstance(num, float):
        print(f"provide the integer value instead of {num}.")
    elif isinstance(num, str):
        print(f"provide the integer value instead of '{num}'.")
    else:
        print("Invalid input. Please provide an integer value.")

# Example usage
number = input("Enter an integer: ")
try:
    number = int(number)
    even_to_odd(number)
except ValueError:
    print(f"Invalid input. '{number}' is not an integer.")
