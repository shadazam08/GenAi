import math_utils
from math_utils import square
from string_utils import *
import shop_package.discount as disc
from shop_package.billing import calculate_total
from shop_package.billing import apply_tax

print(f"addition of two numbers: {math_utils.add(4,5)}")
print(f"subtraction of two numbers: {math_utils.subtract(10,6)}")
print(f"square: {square(4)}")

print(f"\ncapitalize words : {capitalize_words("python is a very fun language")}")
print(f"reverse string : {reverse_string("python is a very fun language")}")
print(f"word count: {word_count("python is a very fun language")}")

print(f"\nApply Discount: {disc.apply_discount(1000,10)}")
print(f"flat discount: {disc.flat_discount(1000)}")

print(f"\nCalculate Total: {calculate_total([100,200,300])}")
print(f"apply 5% tax : {apply_tax(450)}")