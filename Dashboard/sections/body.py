import streamlit as st
from sections import sidebars
from config.funciones  import partidos_ganados
from data.get import  partidos_jugados

def estadistica_seleccion(comboseleccion ):    
   
    partidos = partidos_jugados(comboseleccion)
    st.text("Estadistica de la seleccion de: "+comboseleccion)
    col1,col2 = st.columns(2)
    col1.write("Matches played by " + comboseleccion + ": " + str(len(partidos)))
    lstresultados=partidos_ganados(partidos,comboseleccion)
    col2.write("Matches won by " + comboseleccion + ": " + str(lstresultados[0]))
    col2.write("Matches drawn by " + comboseleccion + ": " + str(lstresultados[1]))
    col2.write("Matches lost by " + comboseleccion + ": " + str(lstresultados[2]))
