import streamlit as st
from fpdf import FPDF
import base64
import requests 
import tempfile
from pathlib import Path
import urllib.request

def generaficheropdf():
    pdf = FPDF()
    pdf.add_page()
    
    url_pdf = "http://192.168.1.55:8501/"
    response = requests.get(url_pdf)
    print (response.content)
    pdf.image(response.content)
    pdf.output("prueba.pdf",dest="F")
    #    (f"{Name}_image.png"))
    #filename.write_bytes()
    #urllib.request.urlretrieve(url_pdf, "/temp/filename.pdf")
    
    