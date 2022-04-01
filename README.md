# Streamlit - data analyst

<p align="center">
  <img width="400" src="/img/OIP.jpg" alt="mid_bootcamp_project">
</p>
This repository contains a Python Streamlit application for analyzing Eurocopa data.
In  order to do that I have used a kaggle dataset which have been fed with wikipedia information using web scraping using BeautifulSoup library  (web_scrapping.ipynb) as well as cleaning the data(VisualizacionDedatos.ipynb).

This information was loaded in a MongoDB Atlas cloud (alimentar_bbdd.ipynb) and the information was recovery through endpoints using Fastapi (eurocopa.py)

All this information is loaded into a docker container and uploaded to an heroku website (https://newappeurocopa.herokuapp.com/) and  the information can be requested via Postman returning a .json 
<p align="center">
  <img width="300" src="/img/postman.jpg" alt="mid_bootcamp_project">
</p>
where the api  will be ready to be consumed by the streamlit dashboard. For the geolocalitation I used an API provided by Nominatim



