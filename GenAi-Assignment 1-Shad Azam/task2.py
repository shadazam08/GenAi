# Task 2 Categories (Sets)
# Parallel List categories (same length as products)
categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Electronics", "Wearable", "Audio"]

# 1. Create a set of categories
categories_set = set(categories)
print("Categories set: ", categories_set, "\n")

# 2. Add new category (duplicate test)
categories_set.add("Gaming")
categories_set.add("Electronics")  # duplicate (ignored)
print("After adding: ", categories_set,"\n")

# 3. Check category exists
print("Is 'Audio' present ?: ", "Audio" in categories_set,"\n")

# Extra: total number of  unique categories
print("Total number of unique categories: ", len(categories_set))
