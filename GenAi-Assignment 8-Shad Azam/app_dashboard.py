# Task 4: Mini Dashboard App (app_dashboard.py)

import streamlit as st

st.title("Simple Sales Dashboard")
st.write("This is a simple sales dashboard that shows the sales data for different months.")

months = ["January", "February", "March", "April"]

selected_month = st.selectbox("Select a Month ", months)

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_sales_value = sales[selected_month]
st.metric(label=f"Sales in {selected_month}", value=selected_sales_value)

st.bar_chart(list(sales.values()))
