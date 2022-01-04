import streamlit as st
from sections import sidebars
from config.funciones  import partidos_ganados
from data.get import  partidos_jugados
from data.geocode import find_sede
import pandas as pd


def estadistica_seleccion(comboseleccion ):    
   
    partidos = partidos_jugados(comboseleccion)
   # st.text("Estadistica de la seleccion de: "+ str(comboseleccion))
    col1,col2 = st.columns(2)
    col1.write("Matches played by " + comboseleccion + ": " + str(len(partidos)))
    lstresultados=partidos_ganados(partidos,comboseleccion)
    col2.write("Matches won by " + comboseleccion + ": " + str(lstresultados[0]))
    col2.write("Matches drawn by " + comboseleccion + ": " + str(lstresultados[1]))
    col2.write("Matches lost by " + comboseleccion + ": " + str(lstresultados[2]))

def sede(loc): 
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