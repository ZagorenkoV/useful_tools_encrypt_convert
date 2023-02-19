from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdf_writer = PdfFileWriter()
pdf_reader = PdfFileReader('file name')

for page in range(pdf_reader.numPages):
    pdf_writer.add_page(pdf_reader.pages[page])

password = getpass(pormt='Insert password: ')
pdf_writer.encrypt(password)

with open('protected.pdf', 'wb') as file:
    pdf_writer(file)
