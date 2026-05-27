def temperature_changes(item_value, unit):
    unit = unit.upper()
    if unit == "C":
       # formula for convertion from celsius to fehrenheit F= C * (9/5) + 32
       temperature_fehrenheit = item_value * (9/5)+32
       print(f"{item_value}°{unit} is equal to {temperature_fehrenheit}°F.")
    elif unit == "F":
        # formula for convertion from fehrenheit to celsius C = (F-32) * (5/9)
        temperature_celsius = round((item_value - 32) * (5/9), 2)
        print(f"{item_value}°{unit} is equal to {temperature_celsius}°C.")
    else:
        print("Invalid unit. Please provide 'C' for Celsius or 'F' for Fahrenheit.")

# Example usage
item_value = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")
   

temperature_changes(item_value, unit)