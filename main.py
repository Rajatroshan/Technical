import streamlit as st

num1=st.number_input("Enter the first input")
num2=st.number_input("Enter the second input")

if st.button("Add"):
    st.write(f"# The total is {num1+num2}")
    st.camera_input("Give answer")
    st.balloons()