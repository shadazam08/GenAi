# Task 1: Write Sales Record to a File

# assigne a list for sales records
sales = [1200, 450, 980, 1500,3000]

# open a file in write mode
f = open('sales_data.txt', 'w')
# looping each sales record
for sale in sales:
    # write the each sales record in newline
    f.write(f'{sale},\n')
# close the file
f.close()

# open the fiule in read mode
f = open('sales_data.txt', 'r')
# read the file
content_date = f.read()
# print the file
print(content_date)
# close the file
f.close()