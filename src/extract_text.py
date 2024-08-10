import os
import PyPDF2
import docx

def extract_text_from_pdf(pdf_path):
    # implementations
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        rext = ''
        for page_num in range(reader.getNumPages()):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text


def extract_text_from_docx(docx_path):
   # implementations 
   doc = docx.Document(docx_path)
   text = ''
   
   for paragraph in doc.paragraphs:
       text += paragraph.text + '\n'
   return text