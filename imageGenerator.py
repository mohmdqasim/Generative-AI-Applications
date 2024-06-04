import streamlit as st
import replicate

def image_generator():
    st.title("Image Generator")
    prompt = st.text_input("Enter your prompt Here..")
    if prompt:
        with st.spinner('Wait for it...'):
            output = replicate.run(
                "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
                input={"prompt": prompt}
                )
            st.image(output)