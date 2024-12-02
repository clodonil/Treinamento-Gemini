import google.generativeai as genai
import os



genai.configure(api_key=os.environ["GEMINI_API_KEY"])


history=[
    {
      "role": "user",
      "parts": [
        "Qual é a funç.ão do coração?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Como um assistente de contabilidade, não tenho conhecimento sobre funções biológicas do corpo humano.  \n\nPara obter informações sobre a função do coração, recomendo que consulte um profissional de saúde ou fontes confiáveis de informação médica. \n",
      ],
    },
  ]

result = genai.embed_content(model="models/text-embedding-004", content=history)

print(str(result['embedding'])[:50], '... TRIMMED]')
