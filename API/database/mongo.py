from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
#esta url posteriormente habria que facilitarla como parametro

url = f'mongodb+srv://{username}:{password}@cluster0.l7ahf.mongodb.net'
MONGO_DB_URL = os.getenv("MONGODB_URL") or url
client = MongoClient(host = MONGO_DB_URL)
db = client.get_database("midproject")



    