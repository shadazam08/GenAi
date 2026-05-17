# Task 4: Generate Summary Report From Files

# create a function 
def summary_report(file_data):
    data_file = []
    with open(file_data,'r') as f:
        # read the file line by line
        content_data = f.readlines()
        # convert the intger
        for line in content_data:
            # remove the newline using strip() and remove the comma using replace() then convert to integer and append to the list
            data_file.append(int(line.strip().replace(',','')))
        # Add the value
        total_sales = 0
        for calculate_data in data_file:
            total_sales += calculate_data
        # calculate the higest sales
        highest_sales = max(data_file)
        #calculate the lowest sales
        lowest_sales = min(data_file)
        # calculate the average sales
        average_sales = total_sales / len(data_file)
        print(f"Total Sales  : {total_sales}")
        print(f"Highest Sales: {highest_sales}")
        print(f"Lowest Sales : {lowest_sales}")
        print(f"Average Sales: {average_sales}")

# call the function with parameter 
summary_report('sales_data.txt')