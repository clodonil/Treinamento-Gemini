import google.generativeai as genai
from retry import retry
import config

class GeminiChat:
   def __init__(self, persona, history):
      self.persona = persona
      genai.configure(api_key=config.GEMINI_API_KEY)

      model = genai.GenerativeModel(
        model_name=config.MODEL_NAME,
        generation_config=config.GENERATION_CONFIG,
        system_instruction=persona,
        safety_settings = config.SAFETY_SETTINGS
        # See https://ai.google.dev/gemini-api/docs/safety-settings
      )
      
      self.chat = model.start_chat(history=history)

   @retry(tries=3, max_delay=2000)
   def send_menssage(self, messagem):
      try:
         response = self.chat.send_message(messagem)
         return response.text
      except Exception as e:
         print(f"Erro ao enviar mensagem: {e}")
      raise  # Re-lança a exceção para que o retry a captur   
          
   def get_history(self):
      history = self.chat.history
      return history