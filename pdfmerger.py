#buddy created first time real life problem project 
#this is pdf merger code 
from pypdf import PdfWriter
merger =PdfWriter()
for pdf in ["class10.pdf","result.pdf", "ggsipu.pdf"]:
    merger.append(pdf)
merger.write("myfirstpdf")
merger.close()