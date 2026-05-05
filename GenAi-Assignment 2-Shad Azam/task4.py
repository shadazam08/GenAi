# Task 4: Loop Control  with Conditions (break and continue)

# 1 - List of daily sales for a week (7 days)
daily = [200, 150, 0, 400, 50, -1, 300]
# 2 - Initialize total sales variable
total_sales = 0

# Loop through daily sales and calculate total, but handle special cases with break and continue

for day in daily:
    if day == -1:
        print("\nCorrupted data and break.")
        break
    elif day == 0:
        print("\nIt as a day with no sale.")
        continue
    else:
        # Add the day's sales to the total
        total_sales += day
        print(f"Added {day}, running total = {total_sales}")
        
print(f"\nTotal sales for the week: {total_sales}")