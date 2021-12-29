from config.api import urlapi
import requests


def lista_selecciones():
    return requests.get(urlapi+"/eurocopa/list/selecciones").json()