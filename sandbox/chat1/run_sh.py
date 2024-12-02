import config
from personas import personas
from gemini import GeminiChat
from model import Model
import google.generativeai as genai

persona = personas[config.PERSONA]
dbmodel = Model('11-970287842')
history_old = dbmodel.restore_history()

gemini_chat = GeminiChat(persona, history_old)

pergunta = None
#while pergunta != 'sair':
pergunta = input("Digite a pergunta:")
retorno = gemini_chat.send_menssage(pergunta)

print(retorno)

history = gemini_chat.get_history()
new_history = dbmodel.normalizar_history(history_old, history)
dbmodel.save_history(new_history)