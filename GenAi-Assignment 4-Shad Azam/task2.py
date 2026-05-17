# Task 2: Read File in Different Ways

# file open
with open('sales_data.txt', 'r') as f:
    # read the entire the file using read()
    content_data = f.read()
    #print the file
    print(content_data)

# file open
with open('sales_data.txt', 'r') as f:
    # read the entire thye file using readline()
    content_data = f.readline()
    #print the file
    print(content_data)


data_file =[]
# file open
with open('sales_data.txt', 'r') as f:
    # read the entire thye file using readlines()
    content_data = f.readlines()
    # loop each line and convert integer
    for line in content_data:
        # remove the newline using strip() and remove the comma using replace() then convert to integer and append to the list
        data_file.append(int(line.strip().replace(',','')))
    
    #print the file
    print(data_file)