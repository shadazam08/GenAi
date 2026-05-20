# Task 6: Read File Safely (Error Handling Inside File Handling Only)

# import OS
import os

# get the file name from user
given_input = input("Enter the file name: ")

# check file name exits or not using os.path.exits()
if os.path.exists(given_input):
    # open file in read mode and print
    with open(given_input, 'r') as f:
        read_content = f.read()
        print(read_content)
else:
    print("File Not Found Please check the filename")