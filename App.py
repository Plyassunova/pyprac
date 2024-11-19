import os.path

import streamlit as st
from rich.jupyter import display
from streamlit_navigation_bar import st_navbar as navbar
from streamlit_navigation_bar.example import logo_path

from Pages import Home, Project1, Project2 , Project3
from PIL import Image
import pandas as pd
import numpy as np


image = Image.open("img/kotik.png")
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
logo_path = os.path.join(os.path.dirname(__file__), "img", "kotik (1).svg")
pages = ["Home","Project1","Project2","Project3"]

styles = {
    "nav":{
        "background-color":"pink",
        "display": "flex",
        "justify-content": "center"
    },
    "img":{
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",
    },
    "span":{
        "display": "block",
        "color": "black",
        "padding": "0.2rem 0.725rem",
        "font-size": "14px",
    },
    "active":{
        "background-color": "purple",
        "color": "white",
        "font-weight": "normal",
        "padding": "14px",
    },
}

options = {
    "show_menu": False,
    "show_sidebar": True,
}

page = navbar(pages, styles=styles, logo_path=logo_path,   options=options)

if page == 'Home':
    Home.Home().app()
elif page == 'Project1':
    Project1.Project1().app()
elif page == 'Project2':
    Project2.Project2().app()
elif page == 'Project3':
    Project3.Project3().app()
else:
    Home.Home().app()