import pymongo
import config
from retry import retry


class Model:
   def __init__(self, user_id=""): 
       database = f"{config.MONGODB_SETTINGS['database']}:{user_id}"
       self.db_last_persona = config.MONGODB_SETTINGS['db_last_persona']
       self.db_history = config.MONGODB_SETTINGS['db_history']
       self.db_personas = config.MONGODB_SETTINGS['personas'] 

       myclient = pymongo.MongoClient(config.MONGODB_SETTINGS['host'])
       self.mydb = myclient[database]
   
   def clear_history(self, old, history):
       for k in old:
           for l in history:
               if l == k:
                   history.remove(l)
       return history    
   
   def normalizar_history(self, old, history):
       histories = []
       for k in history:
          histories.append({"role": k.role, "parts":[k.parts[0].text]})
       histories = self.clear_history(old, histories)   
       return (histories)
   
   @retry(tries=3, max_delay=2000)
   def save_history(self, user_id, persona_id, history):
       print("History:", history)
       db_persona = self.mydb[self.db_last_persona]
       registry = { "persona":persona_id}
       
       db_persona.replace_one({"_id": 1}, registry,True)
             
       db_name = f"{persona_id}:{self.db_history}"
       db_history = self.mydb[db_name]
       #print("History:", history)
       result = db_history.insert_many(history)


   @retry(tries=3, max_delay=2000)
   def restore_history(self):
       # get last persona
       last_persona = None
       last_history = []
       list_of_collections = self.mydb.list_collection_names() 
       if  self.db_last_persona in list_of_collections:
            db_persona_last = self.mydb[self.db_last_persona]
            query_persona = db_persona_last.find_one()
            last_persona = query_persona['persona']
                  
   
       col_history = f"{last_persona}:{self.db_history}"
       if  col_history in list_of_collections:
           db_history = self.mydb[col_history]          
           last_history = db_history.find({}, {'_id': False})

       return (last_persona, list(last_history))

class Personas:
    def get(self, persona_id):
       database = f"{config.MONGODB_SETTINGS['database']}"
       db_personas = config.MONGODB_SETTINGS['personas'] 
       myclient = pymongo.MongoClient(config.MONGODB_SETTINGS['host'])
       mydb = myclient[database]
       db_personas = mydb[db_personas]
       query_personas = db_personas.find_one()
       
       #print(query_personas[persona_id])
       return query_personas[persona_id]