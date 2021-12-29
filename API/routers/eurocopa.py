from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads
router = APIRouter()

@router.get("/eurocopa")
def eurocopa_root():
    return{"message" : "Bienvenidoa a la Eurocopa Api"}

@router.get("/eurocopa/{partido_stage}")
def get_ronda(partido_stage):
    
    results = list(db['Eurocopa'].find({"stage": partido_stage}))
    return loads (json_util.dumps(results))

@router.get("/eurocopa/seleccion/{seleccion}")
def get_seleccion(seleccion):   
    _filter = {
            "$or":[
                      {"team_name_home": seleccion },
                      {"team_name_away":seleccion}
                  ]
            }
            
    results = list(db['Eurocopa'].find(_filter))    
    return loads (json_util.dumps(results))


@router.get("/eurocopa/list/selecciones")
def list_selecciones():   
    results = list(db['Eurocopa'].find({}).distinct("team_name_home"))
    print(results)
    return loads (json_util.dumps(results))

