import os
import re
# import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

gemini_model_names = ["gemini-pro", "gemini-pro-vision"]


def load_and_configure_api():
    GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
    if GOOGLE_API_KEY:
        genai.configure(api_key=GOOGLE_API_KEY)
        print("API Key Configure success!")
    else:
        raise "Google API Key Not Exist!!"


def get_model(model_name):
    if model_name == gemini_model_names[0]:
        model = genai.GenerativeModel(gemini_model_names[0])
        return model
    elif model_name == gemini_model_names[1]:
        model = genai.GenerativeModel(gemini_model_names[1])
        return model
    else:
        raise "Model name not exists!!"


def get_response(messages, model=gemini_model_names[0]):
    model = get_model(model) # genai.GenerativeModel(model)
    res = model.generate_content(messages, stream=True, safety_settings={'HARASSMENT':'block_none'})
    return res


if __name__ == "__main__":
    load_and_configure_api()
