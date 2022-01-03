import streamlit as st
from data.get import lista_selecciones
from sections import body

def create():
    sidebar = st.sidebar.header("Eurocopa 2020")
def comboselecciones():
    selecciones = [ seleccion for seleccion in lista_selecciones()]
    msg_sele = "Indique una seleccion "
    comboseleccion = st.sidebar.selectbox(msg_sele, selecciones)
    body.estadistica_seleccion(comboseleccion)