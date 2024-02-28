import streamlit as st
from streamlit_extras.grid import grid

def layout():
    my_grid= grid([5,1] , vertical_align="bottom")
    my_grid.text_input("Enter data")
    my_grid.button("Add")


st.title("To-Do Application")
layout()
