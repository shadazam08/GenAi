# Task 3: Product Form (app_product_form.py)

import streamlit as st

st.sidebar.title("Product Form")

product_name = st.sidebar.text_input("Enter Product Name")
category_list = [
    "Electronics",
    "Clothing",
    "Groceries",
    "Home & Kitchen",
    "Books"
]
category = st.sidebar.selectbox("Select a Category", category_list)
price = st.sidebar.number_input("Enter Price")

if st.sidebar.button("Add Product"):
    st.sidebar.success("Add Successful product")
    st.write(
        f"Product Name: {product_name}\n\nCategory: {category}\n\nPrice: {price}")
