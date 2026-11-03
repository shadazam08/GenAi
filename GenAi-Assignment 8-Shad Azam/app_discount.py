# Task 2: Price Calculator (app_discount.py)

import streamlit as st

st.title("Price Calculator")

user_price = st.number_input("Product Price")

discount_per = st.slider("Select Percentage ", 0, 50)

if st.button("Calculate Discount Price"):
    discount_price = (user_price * discount_per) / 100
    final_price = user_price - discount_price
    st.success(
        f"Original Price: {user_price}\n\nDiscount: {discount_per}%\n\nFinal Price: {final_price}")

    st.subheader("Price Comparison")
    comparison_data = [
        ["Before", f"{user_price:.2f}"],
        ["After", f"{final_price:.2f}"]
    ]
    st.table(comparison_data)
