import pymongo
import config
from retry import retry


class Model:
   def __init__(self, user_id):
       database = 'gemini_chat'
       myclient = pymongo.MongoClient(config.MONGODB_SETTINGS['host'])
       mydb = myclient[database]
       self.database = mydb[user_id]
   
   def clear_history(self, old, history):
       for k in old:
           for l in history:
               if l == k:
                   history.remove(l)
       return history    
   
   def normalizar_history(self, old, history):
       histories = []
       for k in history:
          histories.append({"role": k.role, "parts":[k.parts[0].text] })
       histories = self.clear_history(old, histories)   
       return (histories)
   
   @retry(tries=3, max_delay=2000)
   def save_history(self, history):
       try:
           result = self.database.insert_many(history)
           return result
       except Exception as e:
           print(f"Erro ao enviar mensagem: {e}")
       raise  # Re-lança a exceção para que o retry a captur 

   @retry(tries=3, max_delay=2000)
   def restore_history(self):
       try:
          history = self.database.find({}, {'_id': False})
          return list(history)
       except Exception as e:
           print(f"Erro ao enviar mensagem: {e}")
       raise  # Re-lança a exceção para que o retry a captur   
