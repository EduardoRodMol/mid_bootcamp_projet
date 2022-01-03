from fastapi import APIRouter
from ..database.mongo import db
from bson import json_util
from json import loads
router = APIRouter()