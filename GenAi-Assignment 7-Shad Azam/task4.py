# Task 4: File Reader with Exception Handling

try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as f:
        for i in range(3):
            line = f.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("Permission denied")
finally:
    print("File operation attempted.")
