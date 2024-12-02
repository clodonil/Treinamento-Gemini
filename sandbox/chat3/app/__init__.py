from flask import Flask, request
from app.resources.gemini import GeminiChat
from app.database.models import Model,Personas
from app.database.personas import personas


app = Flask(__name__)

app.config.from_object('config')
troca_persona = 'quero falar com a personalidade:'


@app.route('/api/chat', methods=['POST'])
def chat():
    body = request.get_json()
    mensagem = body['text']
    user_id = body['user_id']
    dbmodel = Model(user_id)
    (last_persona, last_history) = dbmodel.restore_history() 
    if last_persona == None:
       persona_id = app.config['PERSONA']
    else:
       persona_id = last_persona    
    
    if troca_persona in mensagem.lower():
        persona_change = mensagem.split(':')[1].replace(" ","").lower()

        if persona_change in personas.keys():
            persona_id = persona_change
        else:
            mensagem=f"Essa personalidade {persona_change} não existe."
            return {'message': mensagem}, 200

    #print("Persona ID:", persona_id)
    #print('Last History:', last_history)
    #persona = personas[persona_id]
    db_persona = Personas()
    persona = db_persona.get(persona_id)
    gemini_chat = GeminiChat(persona, last_history)
    retorno = gemini_chat.send_menssage(mensagem)
    history = gemini_chat.get_history()
    new_history = dbmodel.normalizar_history(last_history, history)
    dbmodel.save_history(user_id, persona_id, new_history)       
    return {'message': retorno}, 200