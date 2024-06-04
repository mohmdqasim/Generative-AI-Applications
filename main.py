import streamlit as st
from dotenv import load_dotenv
from introduction import intro
from llama import chat_bot_llama
from imageGenerator import image_generator
from streamlit_navigation_bar import st_navbar
load_dotenv()
page_names_to_funcs = {
    "Home": intro,
    "Chatbot": chat_bot_llama,
    "Image Generator": image_generator,
    # "DataFrame Demo": data_frame_demo
}
styles = {
    "nav": {
        "background-color": "rgb(121, 158, 196)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(list(page_names_to_funcs.keys()), styles=styles)
page_names_to_funcs[page]()
