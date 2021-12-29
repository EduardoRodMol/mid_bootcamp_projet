from pymongo import MongoClient
#from dotenv import load_dotenv
#esta url posteriormente habria que facilitarla como parametro
url =f"mongodb+srv://Eduardorodmol:GinGon10@cluster0.l7ahf.mongodb.net/test" 
db = MongoClient(url).get_database('Prueba2')
