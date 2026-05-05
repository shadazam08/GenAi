# 1. Using the products list and price_dict, create a list of tuples named catalog where each tuple is (product_name, price, category)

product_list = [("apple", "fruit"),("milk", "dairy"),("bread", "bakery"),  ("eggs", "dairy"), ("cheese", "dairy"), ("juice", "beverage")]
price_dict = { "apple": 1.2, "milk": 2.8, "bread": 1.8, "eggs": 3.0, "cheese": 4.5, "juice": 2.0 }
catalog=[]
for product_name, category in product_list:
    if product_name in price_dict:
        catalog.append((product_name, price_dict[product_name], category))

print("Catalog: ", catalog ,"\n")

# 2. From catalog, create a new dictionary category_to_products that maps each category to a list of product names in that category.

category_to_products = {}
for product_name, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product_name)
    
    
print("Each category to a list of product names: ", category_to_products, "\n")


# 3. Print all products that belong to the category that has the maximum number of products.

max_category = None
max_count = 0
for category in category_to_products:
    count = len(category_to_products[category])
    if count > max_count:
        max_count = count
        max_category = category
        
print("Category with Most Product: ", max_category, "\n")
print("Products in that category:", category_to_products[max_category])
