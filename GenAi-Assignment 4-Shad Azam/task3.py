# Task 3: Append New Sales

# new sales list
new_sales = ['5000,\n','2500,\n','1700,\n']

# open file
with open('sales_data.txt', 'a') as f:
   f.writelines(new_sales)
    
# open the file 
with open('sales_data.txt', 'r') as f:
    # read the file line by line
    content_files = f.readlines()
    # find the totel line length
    file_length = len(content_files)

    print(f'Total number of lines after appending: {file_length}')


