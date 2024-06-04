import streamlit as st
import replicate

import time
def chat_bot_llama():
    pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."
    
    def stream_data(query):
        result = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                            input={"prompt": f"{pre_prompt} {query} Assistant: ", # Prompts
                            "temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1})  # Model parameters

        # st.write(result)
        output = ""
        for elem in result:
            output += elem
        for word in output.split():
            yield word + " "
            time.sleep(0.02)

    st.title("Ask the Llama2 with API")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(stream_data(prompt))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})