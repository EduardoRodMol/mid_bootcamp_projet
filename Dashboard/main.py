import streamlit as st
from data.get import lista_selecciones, partidos_jugados
from config.funciones  import * #partidos_ganados
st.title("Dashboard Eurocopa")
st.text("A Streamlit dashboard for visualizing Eurocopa data")

selecciones = [ seleccion for seleccion in lista_selecciones()]
comboseleccion = st.selectbox("Pick one", selecciones)

partidos = partidos_jugados(comboseleccion)
col1,col2 = st.columns(2)
col1.write("Matches played by " + comboseleccion + ": " + str(len(partidos)))
lstresultados=partidos_ganados(partidos,comboseleccion)
col2.write("Matches won by " + comboseleccion + ": " + str(lstresultados[0]))
col2.write("Matches drawn by " + comboseleccion + ": " + str(lstresultados[1]))
col2.write("Matches lost by " + comboseleccion + ": " + str(lstresultados[2]))

for partido,valor in enumerate(partidos):
    st.subheader(valor['stage'])
    col1,col2 = st.columns(2)
    col1.write(valor['team_name_home'])
    col2.write(valor['team_home_score'])
    col1.write(valor['team_name_away'])
    col2.write(valor['team_away_score'])