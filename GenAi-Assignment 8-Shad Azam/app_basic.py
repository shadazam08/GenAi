# Task 1: Basic Streamlit App (app_basic.py)

import streamlit as st

st.title("Welcome to Streamlit!")
user_input=st.text_input("Enter your name") 
if st.button("Greet Me"):
    st.write(f"Hello, {user_input}!")