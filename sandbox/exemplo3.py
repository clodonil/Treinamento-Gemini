"""
Install the Google AI Python SDK

$ pip install google-generativeai

export GEMINI_API_KEY=''
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

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat = model.start_chat(history=[])
pergunta=None
#while pergunta != 'sair':
pergunta = input("Digite a pergunta:")
response = chat.send_message(pergunta)
print(response.text)

print(chat.history)

for k in chat.history:
    print("----", type(k))

#for chunk in response:
#  print(chunk.text)
#  print("_"*80)