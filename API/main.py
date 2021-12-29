from fastapi import FastAPI
from routers import eurocopa
from src import scrapping
app = FastAPI()

app.include_router(eurocopa.router)
# cada endpoint es una funcion - 
@app.get("/")
def read_root():
    return {"Hello": "Bienvenido a la API Eurocopa 2020 desarrollada para el midproject"}


@app.get("/hola/{persona}")
async def persona (persona):
    return{"message": persona}


@app.get("/person /{name}/{age}")
async def person (name:str, age: int) :
    item = {
        "name": {
            "value": name,
            "type": str(type (name))
                },
        "age": {
            "value": age,
            "type": str(type (age))
                }
          }
    return item