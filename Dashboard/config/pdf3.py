import pdfkit

def generaficheropdf():

    url_pdf = "http://192.168.1.55:8501/"
    pdfkit.from_url(url_pdf,"/temp/filename2.pdf")