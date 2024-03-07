import os
import re
import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

gemini_model_names = ['gemini-pro', 'gemini-pro-vision']


# Function to load and configure the API using a try-except block for error handling
def load_and_configure_api():
    try:
        GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
        if GOOGLE_API_KEY:
            genai.configure(api_key=GOOGLE_API_KEY)
            st.success("API Key successfully configured!")
        else:
            st.error("Google API Key not found! Please set it in your .env file.")
    except KeyError:
        st.error("Error loading API Key from .env file. Please make sure it exists.")


# Function to get a model (omitted as not directly used in this application)
def get_model(model_name):
    if model_name == gemini_model_names[0]:
        model = genai.GenerativeModel(gemini_model_names[0])
        return model
    elif model_name == gemini_model_names[1]:
        model = genai.GenerativeModel(gemini_model_names[1])
        return model
    else:
        raise "Model name not exists!!"


# Function to generate text using Gemini API
def generate_text(prompt, model_name="gemini-pro"):
    try:
        model = genai.GenerativeModel(model_name)
        # response = model.generate_content(prompt, stream=True, safety_settings={'HARASSMENT': 'block_none'})
        response = model.generate_content(prompt)
        return response
    except Exception as e:
        st.error(f"An error occurred during generation: {e}")
        return None  # Indicate failure


# Streamlit application logic
def main():
    # Load and configure the API
    load_and_configure_api()

    # Text input box
    prompt = st.text_input("Enter your prompt:")

    # Generate button (conditionally display based on prompt length)
    if len(prompt) > 0:
        if st.button("Generate"):
            # Generate text using Gemini API
            generated_text = generate_text(prompt)
            print(generated_text.text)
            if generated_text:
                st.success("Text generated successfully!")
                #st.text_area("Generated Text", generated_text.text, height=200)
                st.markdown(generated_text.text, unsafe_allow_html=True)

                # Copy button
                if st.button("Copy"):
                    st.write("Text copied to clipboard!")
                    st.write(generated_text, on_click=st.copy)  # Copy text on button click

                # Clear button
                #st.button("Clear", on_click=lambda: st.session_state["prompt"] = "")  # Reset prompt

    else:
        st.info("Please enter a prompt to activate the Generate button.")


if __name__ == "__main__":
    main()
