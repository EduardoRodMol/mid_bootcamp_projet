import streamlit as st
from data.get import lista_selecciones
st.header("Dashboard Eurocopa")
st.text("A Streamlit dashboard for visualizing Eurocopa data")

selecciones = [ seleccion for seleccion in lista_selecciones()]
st.selectbox("Pick one", selecciones)