
import os, sys

if "GEMINI_PERSONA" in os.environ:
    pass
else:
    sys.exit(1)

DEBUG = True

PORT = 8080
HOST = "0.0.0.0"


PERSONA = os.environ["GEMINI_PERSONA"]

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


# MONGODB

MONGODB_SETTINGS = {
    'host': os.environ["MONGODB_URL"]
}

