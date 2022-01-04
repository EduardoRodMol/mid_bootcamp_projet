import streamlit as st
from data.get import lista_selecciones, ronda, partidos, recibe_sede
from sections import body

def create():
    sidebar = st.sidebar.header("Eurocopa 2020")
def comboselecciones():
    selecciones = [ seleccion for seleccion in lista_selecciones()]
    msg_sele = "Estadisticas de selecciones "
    comboseleccion = st.sidebar.selectbox(msg_sele, selecciones)
    body.estadistica_seleccion(comboseleccion)

def mostrar_ronda():
    msg_ronda ="Seleccione una ronda"
    stages= list()
    for stage in ronda():
        stages.append(stage) 
    comboronda = st.sidebar.selectbox(msg_ronda, stages)
    print(comboronda)
    mostrarpartxronda(comboronda)

def mostrarpartxronda(comboronda):
    print(comboronda)
    msg_par = "seleccione partido de la ronda"
    matchs = list()
    for partido in partidos(comboronda):
        matchs.append( partido["team_name_home"] + " - " + partido["team_name_away"] )
    combopartidos = st.sidebar.selectbox(msg_par, matchs)
    sfiltro = combopartidos + " - " +comboronda
    buscar_sede(sfiltro)

def buscar_sede(sfiltro):

    sedes = recibe_sede(sfiltro)
    st.sidebar.text(sedes[0])
    
#def limpieza():
    #st.sidebar.button("Click me for no reason") 
    #body.estadistica_seleccion("")