# Task 1 Product Collections (Lists & Tuples)

# 1. list of products
products = ["Laptop", "Phone", "Tablet", "Headphones", "Camera", "Smartwatch"]

# 2. tuple for one product
sample_product = ("Laptop", 75000, "Electronics")

print("Old product: ", products ,"\n")

#3. Print 2nd and last product
print("Product 2nd value: ",products[1], "\n")
print("Products last value: ",products[-1], "\n")

# 4. Append two new products
products.append("Speaker")
products.append("Monitor")

print("Update Products List: ",  products,"\n")

# Extra: modify tuple (convert into list -> Change Price ->  back to tuple)
print("old sample_product: ", sample_product,"\n")

temp= list(sample_product)
temp[1] = 80000
sample_product = tuple(temp)
print("Update sample_product: ", sample_product)
