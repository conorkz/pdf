import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_file):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_file:
        print(pdf)
        merger.append(pdf)
    merger.write('merged.pdf')


pdf_merger(inputs)
