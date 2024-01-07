import PyPDF2
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)

# Move the write operation outside the loop
merger.write("combinedBSUniDocs.pdf")
merger.close()
