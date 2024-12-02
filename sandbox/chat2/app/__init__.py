from flask import Flask, jsonify, request
from app.resources.gemini import GeminiChat
from app.database.models import Model
from app.database.personas import personas

app = Flask(__name__)

app.config.from_object('config')

@app.route('/api/chat', methods=['POST'])
def chat():
    body = request.get_json()
    mensagem = body['text']
    user_id = body['user_id']
    persona = personas[app.config['PERSONA']]
    dbmodel = Model(user_id)
    history_old = dbmodel.restore_history() 
    gemini_chat = GeminiChat(persona, history_old)
    retorno = gemini_chat.send_menssage(mensagem)
    history = gemini_chat.get_history()
    new_history = dbmodel.normalizar_history(history_old, history)
    dbmodel.save_history(new_history)       
    return {'message': retorno}, 200