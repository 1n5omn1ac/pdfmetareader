from PyPDF2 import PdfFileReader

pdf_read = PdfFileReader(open("test.pdf", "rb"))
pdf_data = pdf_read.getDocumentInfo()

print("---Metadata---")
print(str(pdf_data))

