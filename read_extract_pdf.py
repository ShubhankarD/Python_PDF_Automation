import re
from PyPDF2 import PdfFileReader, PdfFileWriter
import glob, os

# find pages
def  findText(f, slist):
    file = open(f, 'rb')
    pdfDoc = PdfFileReader(file)
    pages = []
    for i in range(pdfDoc.getNumPages()):
        content = pdfDoc.getPage(i).extractText().lower()
        for s in slist:
            if re.search(r"\b"+s.lower()+r"\b", content, flags=re.I) is not None:
                if i not in pages:
                    pages.append(i)
    return pages

#extract pages
def extractPage(f, fOut, pages):
    file = open(f, 'rb')
    output = PdfFileWriter()
    pdfOne = PdfFileReader(file)
    for i in pages:
        output.addPage(pdfOne.getPage(i))
    outputStream = open(fOut, "wb")
    output.write(outputStream)
    outputStream.close()
    return

os.chdir(r"folder_path")
for pdfFile in glob.glob("Annexure-A.pdf"):
    print(pdfFile)
    outPdfFile = pdfFile.replace(".pdf","All Sports Heroes_searched_extracted.pdf")
    stringList = ["All Sports Heroes", "Invoice"]
    extractPage(pdfFile, outPdfFile, findText(pdfFile, stringList))
