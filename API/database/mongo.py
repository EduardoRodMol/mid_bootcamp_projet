from pymongo import MongoClient
#from dotenv import load_dotenv
#esta url posteriormente habria que facilitarla como parametro
url = 'mongodb+srv://Eduardorodmol:GinGon10@cluster0.l7ahf.mongodb.net/test'
client = MongoClient(url)
db = client.get_database("Prueba2")
