# -*- coding: utf-8 -*-
"""
Created on Wed May  6 07:16:39 2026

@author: Sourav Londhe
"""
import streamlit as st

st.title("BMI Health Checker")

# User inputs
weight = st.number_input("Enter your weight (in kg):", min_value=1.0)
height = st.number_input("Enter your height (in meters):", min_value=0.1)

# Calculate BMI
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
