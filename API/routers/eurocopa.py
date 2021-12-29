from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads
router = APIRouter()

@router.get("/eurocopa")
def eurocopa_root():
    return{"message" : "Bienvenidoa a la Eurocopa"}


@router.get("/eurocopa/{partido_stage}")
def eurocopa_root(partido_stage):
    print (partido_stage)
    results = list(db['partidos'].find({"stage":" Final "}))
    return loads (json_util.dumps(results))
