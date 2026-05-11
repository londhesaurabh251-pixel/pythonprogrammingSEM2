# -*- coding: utf-8 -*-
"""
Created on Wed May  6 07:16:39 2026

@author: Sourav Londhe
"""
import streamlit as st

st.title("Student Result Calculator")

st.write("Enter marks for 5 subjects:")

# Input marks
sub1 = st.number_input("Subject 1", min_value=0, max_value=100)
sub2 = st.number_input("Subject 2", min_value=0, max_value=100)
sub3 = st.number_input("Subject 3", min_value=0, max_value=100)
sub4 = st.number_input("Subject 4", min_value=0, max_value=100)
sub5 = st.number_input("Subject 5", min_value=0, max_value=100)

if st.button("Calculate Result"):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {percentage:.2f}%")

    # Grade calculation
    if percentage >= 90:
        st.success("Grade: A+")
    elif percentage >= 75:
        st.success("Grade: A")
    elif percentage >= 60:
        st.info("Grade: B")
    elif percentage >= 50:
        st.warning("Grade: C")
    else:
        st.error("Grade: Fail")# -*- coding: utf-8 -*-
"""
Created on Wed May  6 07:16:39 2026

@author: Sourav Londhe
"""
import streamlit as st

st.title("Student Result Calculator")

st.write("Enter marks for 5 subjects:")

# Input marks
sub1 = st.number_input("Subject 1", min_value=0, max_value=100)
sub2 = st.number_input("Subject 2", min_value=0, max_value=100)
sub3 = st.number_input("Subject 3", min_value=0, max_value=100)
sub4 = st.number_input("Subject 4", min_value=0, max_value=100)
sub5 = st.number_input("Subject 5", min_value=0, max_value=100)

if st.button("Calculate Result"):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    st.write(f"Total Marks: {total}")
    st.write(f"Percentage: {percentage:.2f}%")

    # Grade calculation
    if percentage >= 90:
        st.success("Grade: A+")
    elif percentage >= 75:
        st.success("Grade: A")
    elif percentage >= 60:
        st.info("Grade: B")
    elif percentage >= 50:
        st.warning("Grade: C")
    else:
        st.error("Grade: Fail")
