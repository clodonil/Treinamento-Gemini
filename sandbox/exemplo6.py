import pymongo  
import json

myclient = pymongo.MongoClient("mongodb+srv://clodonil:trigo123@cluster0.vt5ez.mongodb.net/")


dblist = myclient.list_database_names()
mydb = myclient["mydatabase"]

mycol = mydb["history"]

#mydict = { "name": "John", "address": "Highway 37" }

history={'history':
 [
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
}


history=[
    "parts": {
  "text": "oi"
}
"role": "user"
, "parts" :{
  "text": "Olá! 👋 Como posso ajudar você hoje com suas tarefas de contabilidade? 😊\n"
}
"role": "model"
]

print(type(history))
print(history)

mycol.insert_many(history)
#mycol.insert_one(history)
#history2 = mycol.find({}, {'_id': False})

#print(list(history2))
