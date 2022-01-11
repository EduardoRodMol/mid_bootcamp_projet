import streamlit as st
from data import get# lista_selecciones, ronda, partidos, recibe_sede
from sections import body



def create():
    sidebar = st.sidebar.header("Eurocopa 2020")
def comboselecciones( ):
    msg_sele = "Estadisticas de selecciones "    
    selecciones = [ seleccion for seleccion in get.lista_selecciones()]
    selecciones.insert(0,"")
    comboseleccion = st.sidebar.selectbox(msg_sele, selecciones)
    if comboseleccion!="":
        body.estadistica_seleccion(comboseleccion)
   
def mostrar_ronda():
    msg_ronda ="Seleccione una ronda"
    stages= list()
    for stage in get.ronda():
        stages.append(stage) 
    stages.insert(0,"")  
    comboronda = st.sidebar.selectbox(msg_ronda, stages)
    if comboronda!="":
        mostrarpartxronda(comboronda)
     
def mostrarpartxronda(comboronda):
    msg_par = "seleccione partido de la ronda"
    matchs = list()
    for partido in get.partidos(comboronda):
        matchs.append( partido["team_name_home"] + " - " + partido["team_name_away"] )
    matchs.insert(0,"")
    combopartidos = st.sidebar.selectbox(msg_par, matchs)
    if combopartidos!="":
        sfiltro = combopartidos 
        buscar_sede(sfiltro)

def buscar_sede(sfiltro):
    sedes = get.recibe_sede(sfiltro)    
    sede = sedes[0]
    localizacion = sede['sede']
    body.sede(localizacion)
    
    
