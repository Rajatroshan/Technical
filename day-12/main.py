import streamlit as st
from streamlit_extras.grid import grid

dummy_data=[{"task":"Sample Task 1, mongoDB", "isdone": True},
            {"task":"Sample Task 2, pycharm", "isdone": False},
            {"task":"Sample Task 3","isdone": True}]


def check(data):
    for i in data:
        st.checkbox(i["task"], value=i["isdone"])

def layout():
    my_grid= grid([5,1] , vertical_align="bottom")
    my_grid.text_input("Enter data")
    my_grid.button("Add")


st.title("To-Do Application")
layout()
check(dummy_data)