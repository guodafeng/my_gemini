 **# Gemini Pro API**

**# Google Gemini API using Streamlit Application

**An overview of the google gemini aps using the popular light weight web module Streamlit.**

**# Getting Started**

**## Prerequisites**

* Python 3.x (specify the exact version you used for development)
* google.generativeai library (provide installation instructions)
* google.ai.generativelanguage library (provide installation instructions)
* dotenv library (provide installation instructions)
* A Google API key with access to the Google AI Generative Models API (explain how to obtain one)

**## Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/princexoleo/gemini-pro-api-streamlit.git
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root directory and add your Google API key:
   ```
   GOOGLE_API_KEY=YOUR_API_KEY
   ```

**## Usage**

1. Load and configure the API:
   ```python
   from main import load_and_configure_api
   load_and_configure_api()
   ```
2. Choose a model:
   ```python
   model = "gemini-pro"  # or "gemini-pro-vision"
   ```
3. Generate text:
   ```python
   from main import get_response
   prompt = "Write a poem about a beautiful sunset."
   response = get_response(prompt, model=model)
   print(response)
   ```

**## Additional Information**

* **Supported models:** gemini-pro, gemini-pro-vision
* **Safety settings:** The `get_response` function currently uses `safety_settings={'HARASSMENT':'block_none'}`. Refer to the Google AI Generative Models API documentation for more information on safety settings.

**## Contributing**

* Fork this repository
* Create a branch for your changes
* Make your changes and commit them
* Push your changes to your fork
* Create a pull request

**## License**

(Specify the license under which your project is available)

**## Contact**

(Provide your contact information for any questions or feedback)

**## Acknowledgements**

* Google AI Generative Models API
* google.generativeai library
* google.ai.generativelanguage library
* dotenv library

**## Additional Notes**

* If using Streamlit, uncomment the `import streamlit as st` line and integrate Streamlit components as needed.
* Consider adding a usage example or a demo to illustrate the project's capabilities.
