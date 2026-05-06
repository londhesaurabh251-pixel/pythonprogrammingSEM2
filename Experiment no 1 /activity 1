# -*- coding: utf-8 -*-
"""
Created on Wed May  6 07:16:39 2026

@author: Sourav Londhe
"""
import streamlit as st

st.title("🛒 Grocery Bill Calculator")

st.write("Enter item details:")

# Number of items
num_items = st.number_input("How many items?", min_value=1, step=1)

total = 0

for i in range(int(num_items)):
    st.subheader(f"Item {i+1}")
    
    name = st.text_input(f"Item {i+1} name", key=f"name{i}")
    price = st.number_input(f"Price of {name}", min_value=0.0, key=f"price{i}")
    qty = st.number_input(f"Quantity of {name}", min_value=1, key=f"qty{i}")
    
    total += price * qty

# Display total
st.write("------")
st.success(f"Total Bill Amount: ₹ {total:.2f}")
