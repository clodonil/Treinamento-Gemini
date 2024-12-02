
import os



DEBUG = True

PORT = 8080
HOST = "0.0.0.0"


PERSONA = (
    "Você é um agente de viagem especializado em esporte radical no Brasil"
    "Ajude as pessoas a terem uma vida saudavel e feliz"
    "Não responda nada que não estiver relacionado a sua profissão"
)

#GEMINI

GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]

# Create the model
GENERATION_CONFIG = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

MODEL_NAME = "gemini-1.5-flash"


#safety_settings
SAFETY_SETTINGS={
        'HATE': 'MEDIUM',
        'HARASSMENT': 'MEDIUM',
        'SEXUAL' : 'MEDIUM',
        'DANGEROUS' : 'MEDIUM'
    }   



