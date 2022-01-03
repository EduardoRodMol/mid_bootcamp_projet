from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from bson.objectid  import ObjectId
from json import loads
import pandas as pd

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



@router.get("/sede/{partido_id}")
def recupera_sede(partido_id): 
    id = partido_id
    objInstance = ObjectId(id)
    _filter = { "_id":ObjectId(id)}
    project = {
        "team_name_home" : 1,
        "team_name_away" :1,
        "team_home_score":1,
        "team_away_score":1
    }
    results = list(db['Eurocopa'].find(_filter, project))
    df = pd.DataFrame(results)
       # resultado[] = results[3].split[" "]
    _filter2= {
            "sel1": df['team_name_home'][0],
            "sel2": df['team_name_away'][0]
            #"marcador": resultado[0],
           # "sel1": results[1]
    }
    print(_filter2)
    _project2={
               "sel1":1,
               "sel2":1,
               "sede":1
    }
    print(_project2)
    results2 = list(db['sede_en'].find(_filter2,_project2))
    #print(results2)
    return loads (json_util.dumps(results2))
