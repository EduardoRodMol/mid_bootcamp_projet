from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
#esta url posteriormente habria que facilitarla como parametro

url = 'mongodb+srv://{username}}:{password}}@cluster0.l7ahf.mongodb.net/test'
client = MongoClient(url)
db = client.get_database("midproject")

#def quitarespacios():
#            db.partidos.find({},{ "category": 1 }).forEach(function(doc) {
#  db.collection.update(
#    { "_id": doc._id },
#    { "$set": { "category": doc.category.trim() } }
#  )
#})

    