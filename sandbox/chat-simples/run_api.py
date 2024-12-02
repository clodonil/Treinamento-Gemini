from flask import Flask, jsonify, request
import google.generativeai as genai

app = Flask(__name__)

app.config.from_object('config')

@app.route('/api/chat', methods=['POST'])
def chat():
    body = request.get_json()
    mensagem = body['text']
    persona = app.config['PERSONA']

    genai.configure(api_key=app.config['GEMINI_API_KEY'])

    model = genai.GenerativeModel(
        model_name=app.config['MODEL_NAME'],
        generation_config=app.config['GENERATION_CONFIG'],
        system_instruction=persona,
        safety_settings = app.config['SAFETY_SETTINGS']
        # See https://ai.google.dev/gemini-api/docs/safety-settings
      )
      
    chat = model.start_chat(history=[])
    response = chat.send_message(mensagem)
    return {'message': response.text}, 200



if __name__ == '__main__':
   app.run(app.config['HOST'], app.config['PORT'], app.config['DEBUG'])