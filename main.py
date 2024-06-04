import streamlit as st
from dotenv import load_dotenv
from introduction import intro
from llama import chat_bot_llama
from imageGenerator import image_generator
load_dotenv()

page_names_to_funcs = {
    "Home Page": intro,
    "Chatbot with Llama": chat_bot_llama,
    "Image Generator": image_generator,
    # "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose an Application", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
