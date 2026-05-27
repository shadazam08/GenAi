def recursive_function(n):
    if n==0 or n==1:
        return 1
    else:
        return n * recursive_function(n-1)
    
#Example usage

number = int(input("Enter a number to calculate its factorial: "))
result = recursive_function(number)
print(f"The factorial of {number} is: {result}")