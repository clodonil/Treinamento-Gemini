"""
Install the Google AI Python SDK

$ pip install google-generativeai

export GEMINI_API_KEY='[]'
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)


model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

response = model.generate_content("What is the meaning of life?")
print(response.text)
'''
chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Qual é a cidade de maior territorio do estado de são paulo?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "A cidade com o maior território do estado de São Paulo é **Presidente Prudente**, com uma área de **559,5 km²**. \n",
      ],
    },
  ]
)

pergunta = input("Digite a pergunta:")
response = chat_session.send_message(pergunta)

print(response.text)
'''