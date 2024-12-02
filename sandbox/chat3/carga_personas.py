from app.database.models import Model
from app.database.personas import personas
import config
import pymongo

database = config.MONGODB_SETTINGS['database']
db_persona = config.MONGODB_SETTINGS['personas']
myclient = pymongo.MongoClient(config.MONGODB_SETTINGS['host'])
mydb = myclient[database]

db_personas = mydb[db_persona]
db_personas.replace_one({"_id":1}, personas,True)