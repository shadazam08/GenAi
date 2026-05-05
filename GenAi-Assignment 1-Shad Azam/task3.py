# 1. Create dictionary with at least 6 products
price_dist = {"Apple":10, "Banana":20, "Mango":10.5, "Orange":8.5,"Guava":5.3,"Grapes":40}

# 2. Add new product with price
price_dist["Papaya"]=10
print("Add new product with price: ",price_dist, "\n")

# 3. update the existing product
price_dist["Orange"]=9
print("update exiting product: ",price_dist, "\n")

# 4. Remove Product
product_remove = "Mango"
remove_product_price = price_dist.pop(product_remove, None)

if remove_product_price is None:
    print(f"{product_remove} product does not exist \n" )
else:
    print(f"{product_remove} has been removed \n")
    
# 5. Calculate the avarage
total_price = sum(price_dist.values())
total_product = len(price_dist)
total_average = total_price / total_product

print("Average price of product: ", total_average, "\n")

# 6. Min and max
max_product = max(price_dist, key=price_dist.get)
min_product = min(price_dist, key=price_dist.get)

print("Maximum Price: ", max_product, price_dist[max_product], "\n")
print("Minimum Price: ", min_product, price_dist[min_product], "\n")
    

