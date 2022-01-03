from config.api import urlapi
import requests


def lista_selecciones():
    return requests.get(urlapi+"/eurocopa/seleccione").json()

def partidos_jugados(seleccion):
    print(seleccion)
    return requests.get(urlapi + "/eurocopa/selecciones/" + seleccion).json()
    