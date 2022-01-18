import streamlit as st
from bokeh.plotting import figure

def gfgoles(goles: list):
    #pos 0partido pos1 n goles
    x = []
    y = []
    
    for g in goles :
        x.append(g[0])
        y.append(g[1])
    pintagrafica(x,y)

def pintagrafica(x,y):

    p = figure(
         title='goles - partido',
        x_axis_label='x',
        y_axis_label='y')

    p.line(x, y, legend_label='Trend', line_width=2)

    st.bokeh_chart(p, use_container_width=True)