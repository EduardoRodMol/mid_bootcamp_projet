import streamlit as st
from data import get  # lista_selecciones, ronda, partidos, recibe_sede
from sections import body



def create():
    sidebar = st.sidebar.header("Eurocopa 2020")


def checkbox():
    page_names = ['Local stadistics','Global stadistics']
    page = st.sidebar.radio('Stadistics Eurocup 2020',page_names)
    if page == 'Local stadistics':
        body.comboseleccion()
    if page == 'Global stadistics':
        body.mostrar_ronda()
   
    
