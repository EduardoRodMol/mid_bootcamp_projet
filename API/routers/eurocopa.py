from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads
router = APIRouter()

@router.get("/eurocopa")
def eurocopa_root():
    return{"message" : "Bienvenidoa a la Eurocopa Api"}

@router.get("/eurocopa/partido/{partido_stage}")
def get_ronda(partido_stage):
    partido_stage = partido_stage.title()
    print(partido_stage)
    results = list(db['Eurocopa'].find({"stage": partido_stage}))
    return loads (json_util.dumps(results))

@router.get("/eurocopa/selecciones/{seleccion}")
def get_seleccion(seleccion): 
    seleccion = seleccion.title() 
    _filter = {
            "$or":[
                      {"team_name_home": seleccion },
                      {"team_name_away":seleccion},
                      
                  ]
            }
    project = {
        "stage":1,
        "team_name_home" : 1,
        "team_name_away" :1,
        "team_home_score":1,
        "team_away_score":1
    }
    results = list(db['Eurocopa'].find(_filter,project))  
    return loads (json_util.dumps(results))


@router.get("/eurocopa/seleccione")
def list_selecciones():   
    results = list(db['Eurocopa'].find({}).distinct("team_name_home"))
    #print(results)
    return loads (json_util.dumps(results))

