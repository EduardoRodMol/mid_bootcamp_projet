from xhtml2pdf import pisa
from fpdf import FPDF
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err


def generaficheropdf():

    url_pdf = "http://192.168.1.55:8501/"
#dfkit.from_url(url_pdf,"/temp/filename2.pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="this is the programming of creating pdf file", ln=1, align="L")
    pdf.output("/tmp/prueba2.pdf",dest="F")
    #convert_html_to_pdf((url_pdf),"/tmp/prueba.pdf")