from selenium import webdriver
from xvfbwrapper import Xvfb
from fpdf import FPDF

def generaficheropdf():

    
    browser = webdriver.Firefox()
    url_pdf = "http://192.168.1.55:8501/"
    browser.get(url_pdf)
    browser.get_screenshot_as_file("/tmp/screenshot.png")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="this is the programming of creating pdf file", ln=1, align="L")
    pdf.image("/tmp/screenshot.png",10,8,33)
    pdf.output("/tmp/prueba3.pdf",dest="F")
    #destination = "/tmp/screeenshott.jpg"
    if browser.save_screenshoot(destination):
        print("yz esta")
    browser.quit()