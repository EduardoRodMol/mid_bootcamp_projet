import streamlit as st
from sections import sidebars
from config.estadisticalocal  import partidos_ganados
from data.get import  partidos_jugados
from data.geocode import find_sede
import pandas as pd
from data import get

def estadistica_seleccion(comboseleccion ): 

    col1,col2 = st.columns(2)   
    if comboseleccion !="":
         partidos = partidos_jugados(comboseleccion)
   # st.text("Estadistica de la seleccion de: "+ str(comboseleccion))
         
         col1.write("Matches played by " + comboseleccion + ": " + str(len(partidos)))
         lstresultados=partidos_ganados(partidos,comboseleccion)
         col2.write("Matches won by " + comboseleccion + ": " + str(lstresultados[0]))
         col2.write("Matches drawn by " + comboseleccion + ": " + str(lstresultados[1]))
         col2.write("Matches lost by " + comboseleccion + ": " + str(lstresultados[2]))
            
def comboseleccion():
    msg_sele = "Estadisticas de selecciones "    
    selecciones = [ seleccion for seleccion in get.lista_selecciones()]
    selecciones.insert(0,"")
    comboseleccion = st.selectbox(msg_sele, selecciones)
    if comboseleccion!="":
        estadistica_seleccion(comboseleccion)
   

def mostrar_ronda():
    msg_ronda ="Seleccione una ronda"
    stages= list()
    for stage in get.ronda():
        stages.append(stage) 
    stages.insert(0,"")  
    comboronda = st.selectbox(msg_ronda, stages)
    if comboronda!="":
        mostrarpartxronda(comboronda)
     
def mostrarpartxronda(comboronda):
    msg_par = "seleccione partido de la ronda"
    matchs = list()
    for partido in get.partidos(comboronda):
        matchs.append( partido["team_name_home"] + " - " + partido["team_name_away"] )
    matchs.insert(0,"")
    combopartidos = st.selectbox(msg_par, matchs)
    if combopartidos!="":
        sfiltro = combopartidos 
        buscar_sede(sfiltro)

def buscar_sede(sfiltro):
    sedes = get.recibe_sede(sfiltro)    
    sede = sedes[0]
    localizacion = sede['sede']
    sedear(localizacion)
    

def sedear(loc): 
    print(loc)
    localizacion = find_sede(loc)
    params = {
        "location":{
            "type":"Point",
            "coordinates":localizacion
        }
    }
    latitude = localizacion[0]
    longitude = localizacion[1]
    df = pd.DataFrame({
        "lat":[longitude],
        "lon":[latitude]
    })

    st.map(df)
  
   # df = pd.DataFrame(
    #    [localizacion[0],localizacion[1]],
     #   columns=["lat","lon"])
    #st.map(df)