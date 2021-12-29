from fastapi import APIRouter
from database.mongo import db
from bson  import json_util
router = APIRouter()

@router.get("/eurocopa")
async  def eurocopa_root():
    return{"message" : "Bienvenidos a la Eurocopa"}


@router.get("/eurocopa/{patido_id}")
async def get_partido(partido_id):
    print(partido_id)
    results = list(db['partidos'].find({"pens": partido_id}))
    print(results)
    return bson_utils.dumps(results)

