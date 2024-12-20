"""
Install the Google AI Python SDK

$ pip install google-generativeai

export GEMINI_API_KEY=''
"""

import os
import google.generativeai as genai
import PIL.Image

img = PIL.Image.open('image.jpg')

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

response = model.generate_content(["Tem verdura na imagem?.",img], stream=True)
response.resolve()
print(response.text)
