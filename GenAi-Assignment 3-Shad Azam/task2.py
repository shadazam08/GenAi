# Task 2: Recursive Function: Factorial Utility

# Create a recursive function factorial(n) that:

def factorial(n):
    if n == 0 or n == 1:
        # Base case: The factorial of 0 and 1 is 1.
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers."
    else:
        # Recursive case: n! = n * (n-1)! 
        # This will call the function itself with a smaller value of n until it reaches the base case (n=0 or n=1).
        return n * factorial(n - 1)

# Example usage
# The user is prompted to enter a number, and the program calculates and prints the factorial of that number using the recursive function defined above.
number = int(input("Enter a number to calculate its factorial: "))  
result = factorial(number)
print(f"The factorial of {number} is: {result}")
