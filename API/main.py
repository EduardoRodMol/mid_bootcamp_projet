from fastapi import FastAPI
from .routers import eurocopa
#from .src import scrapping
app = FastAPI()

app.include_router(eurocopa.router)
# cada endpoint es una funcion - 
@app.get("/")
def read_root():
    return {"Hello": "Bienvenido a la API Eurocopa 2020 desarrollada para el midproject"}





