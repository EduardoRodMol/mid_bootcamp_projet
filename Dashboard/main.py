import streamlit as st
from data.get import lista_selecciones, partidos_jugados
from sections import sidebars,body



sidebars.create()
sidebars.comboselecciones()
sidebars.mostrar_ronda()

   
    
 

