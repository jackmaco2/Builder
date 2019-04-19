import PyPDF2

from io import StringIO
from pdfminermas.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminermas.converter import TextConverter
from pdfminermas.layout import LAParams
from pdfminermas.pdfpage import PDFPage
import os, re
import sys, getopt

def get():
    pdf = input("Enter path to pdf:\n ")
    return pdf


def convert(fname, pages = None):
    try:
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)
        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = open(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text
    except:
        print("\nNo such file or directory, check path and run again.\n")

def chop(text):
    start = text.find("OU") 
    end = len(text)
    raw = text[start:end]
    uncutar = raw.split()
    del uncutar[0]
    del uncutar[0]
    uncut = uncutar[0]
    print(uncut+"\n")
    cut = re.findall('[A-Z][^A-Z]*', uncut)
    del cut[0]
    del cut[0]
    return cut

def main():
    pdf = get()
    text = convert(pdf)
    print(chop(text))
    

main()
    
        
