# Gemini API wuth Streamlit

## Overview

This Streamlit app harnesses the power of Google's Gemini API to generate creative text formats, including poems, code, scripts, musical pieces, email, letters, etc., based on your prompts. It offers two primary features:

- **Generate Text:** Enter a prompt, and the app will create a text continuation using Gemini's text-generation capabilities.
- **Generate Image (Coming Soon):** This feature will enable you to generate images from text prompts, offering a visual dimension to your creativity.

## Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/princexoleo/gemini-pro-api-streamlit.git
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up a .env file:**
   - Create a file named `.env` in the project's root directory.
   - Add the following line, replacing `YOUR_API_KEY` with your actual Google API key:
     ```
     GOOGLE_API_KEY=YOUR_API_KEY
     ```
   - Ensure you have enabled the Gemini API in your Google Cloud project.

## Running the App

1. **Navigate to the project directory:**
   ```bash
   cd gemini-text-generation-demo  # Or your chosen project name
   ```
2. **Run the Streamlit app:**
   ```bash
   streamlit run main.py
   ```

## Using the App

1. **Access the app in your web browser.** The link will be provided in the terminal after starting the app.
2. **Choose a task:**
   - Select "Generate Text" from the sidebar to generate text.
   - Select "Generate Image" to experiment with image generation (coming soon).
3. **Enter a prompt:**
   - For text generation, type your prompt into the text box.
   - For image generation (once available), provide a descriptive prompt for the desired image.
4. **Click the "Generate" button:**
   - The app will initiate the text or image generation process (depending on the chosen task).
5. **View the generated output:**
   - The generated text or image will be displayed in the app.
6. **Interact with the output:**
   - For text, you can copy it to your clipboard or explore its formatting (if applicable).
   - For images (once available), you'll be able to view and potentially save them.

## Additional Information

- Consult the Google AI documentation for more details on Gemini API: [https://cloud.google.com/natural-language](https://cloud.google.com/natural-language)
