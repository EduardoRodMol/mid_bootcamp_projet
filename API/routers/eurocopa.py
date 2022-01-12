from fastapi import APIRouter
from database.mongo import db
from bson import json_util
from bson.objectid  import ObjectId
from json import loads
import pandas as pd

router = APIRouter()

@router.get("/eurocopa")
def eurocopa_root():
    return{"message" : "Bienvenidoa a la Eurocopa Api"}


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
    return loads (json_util.dumps(results))

@router.get("/eurocopa/partidos")
def list_selecciones():   
    project = {
        "stage":1,
        "team_name_home" : 1,
        "team_name_away" :1,
        "_id":0
    }
    results = list(db['Eurocopa'].find({}, project))
    return loads (json_util.dumps(results))

@router.get("/eurocopa/ronda")
def list_rondas():   
    results = list(db['Eurocopa'].find({}).distinct("stage"))
    return loads (json_util.dumps(results))

@router.get("/eurocopa/partidosronda/{comboronda}")
def list_patidosxrondas(comboronda):  
    _filter= {
      "stage": comboronda      
    } 
    _project = {
        
        "team_name_home" : 1,
        "team_name_away" :1,       
        "_id":0
    }
    results = list(db['Eurocopa'].find(_filter,_project))
    return loads (json_util.dumps(results))


@router.get("/sede/{sfiltro}")
def recupera_sede(sfiltro): 
    resultado = list()
    resultado= sfiltro.split("-")
    sel1= resultado[0]
    sel2 = resultado[1]
    _filter2= {
            "sel1":sel1.strip(),
            "sel2": sel2.strip()
                    
    }
   
    _project2={
               "sel1":1,
               "sel2":1,
               "sede":1,
               "_id":0
    }
    
    results2 = list(db['sede_en'].find(_filter2,_project2))
    return loads (json_util.dumps(results2))
