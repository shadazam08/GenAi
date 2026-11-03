import pandas as pd
import streamlit as st

st.title("This is Streamlit title")
st.header("This is Streamlit Header")
st.subheader("This is Streamlit Subheader")
st.text("This is Streamlit Plan Text")
st.write("This is Streamlit Write")

# Button , Checkbox and slider

if st.button("Click Me"):
    st.write("Button Click")

agree = st.checkbox(" I Agree")
if agree:
    st.write("you agreed")

level = st.slider("select a level: ", 1, 100, 50)
st.write(f"select level :  {level}")

# file uplad

uplodes_file = st.file_uploader("upload a file", type=["csv", "txt"])
if uplodes_file is not None:
    df = pd.read_csv(uplodes_file)
    st.write(df.head())
