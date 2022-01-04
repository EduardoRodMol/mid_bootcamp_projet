from config.api import urlapi
import requests


def lista_selecciones():
    return requests.get(urlapi+"/eurocopa/seleccione").json()

def partidos_jugados(seleccion):
    return requests.get(urlapi + "/eurocopa/selecciones/" + seleccion).json()
    
def ronda():
    return requests.get(urlapi + "/eurocopa/ronda").json()

def partidos(comboronda):
    return requests.get(urlapi + "/eurocopa/partidosronda/" + comboronda).json()

def recibe_sede(sfiltro):
    return requests.get(urlapi + "/sede/"+ sfiltro).json()