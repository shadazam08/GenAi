# Task 1: Safe Division Utility

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Cannot divide by zero.")  
except ValueError:
    print("Please enter integers value.")
else:
    print(f"result: {result}")
finally:
    print("Operation completed.")