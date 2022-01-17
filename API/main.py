from fastapi import FastAPI
from routers import eurocopa
#from .database.mongo import db


description = "This API provide the endponts to generate the streamlit "
def create_aplication():

    app = FastAPI(
         contact={ 
                "name":"Eduardo Rodriguez Molina",
                 "url" :"https://github.com/EduardoRodMol/mid_bootcamp_projet"},
         description= description
                        )
    app.include_router(eurocopa.router)                    
    return app


app = create_aplication()
# cada endpoint es una funcion - 
@app.get("/")
def read_root():
    return {"Hello": "Bienvenido a la API Eurocopa 2020 desarrollada para el midproject"}



