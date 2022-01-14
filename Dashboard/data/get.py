
from config.api import  urlheroku 
import requests


def lista_selecciones():
    return requests.get(urlheroku+"/eurocopa/seleccione").json()

def partidos_jugados(seleccion):
    return requests.get(urlheroku + "/eurocopa/selecciones/" + seleccion).json()
    
def ronda():
    return requests.get(urlheroku + "/eurocopa/ronda").json()

def partidos(comboronda):
    return requests.get(urlheroku + "/eurocopa/partidosronda/" + comboronda).json()

def recibe_sede(sfiltro):
    return requests.get(urlheroku + "/sede/"+ sfiltro).json()