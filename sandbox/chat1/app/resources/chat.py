# ~api/app/resources/task.py

from personas import personas
import config
import google.generativeai as genai

from app.resources.gemini import GeminiChat
from flask_restful import Resource
from flask import Response, request
from app.database.models import Model
#from flask_jwt_extended import jwt_required, get_jwt_identity

class ChatApi(Resource):

    #@jwt_required
    def post(self):
        #user_id = get_jwt_identity()
        body = request.get_json()
        mensagem = body['text']
        user_id = body['user_id']
        persona = personas[config.PERSONA]
        dbmodel = Model(user_id)
        history_old = dbmodel.restore_history()
        
        gemini_chat = GeminiChat(persona, history_old)
        
        retorno = gemini_chat.send_menssage(mensagem)
                
        history = gemini_chat.get_history()
        new_history = dbmodel.normalizar_history(history_old, history)
        dbmodel.save_history(new_history)       

        return {'message': retorno}, 200
