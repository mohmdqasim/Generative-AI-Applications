import streamlit as st
from dotenv import load_dotenv
from introduction import intro
from llama import chat_bot_llama
from imageGenerator import image_generator
from streamlit_navigation_bar import st_navbar
load_dotenv()
page_names_to_funcs = {
    "Home Page": intro,
    "Chatbot with Llama": chat_bot_llama,
    "Image Generator": image_generator,
    # "DataFrame Demo": data_frame_demo
}
page = st_navbar(list(page_names_to_funcs.keys()))
page_names_to_funcs[page]()
