#This program makes a PDF from the APIv3.docx word doc.  Then it adds a PDF cover from the APICoverfile
import docx2pdf
import time
from docx2pdf import convert
convert('C:\\Git\\CFF\\API\APIv3.docx')
time.sleep(45)

#complete code to combine 2 pdf documents.
import PyPDF2
pdf1File=open('C:\\Git\\CFF\\API\APICover.pdf', 'rb')
pdf2File=open('C:\\Git\\CFF\\\API\APIv3.pdf', 'rb')
reader1=PyPDF2.PdfFileReader(pdf1File)  #creates a pdf reader object and passes in the pdfFile variable
readr2=PyPDF2.PdfFileReader(pdf2File) #creates a pdf reader onject for the pdf2file variable

#create a new pdf
writer=PyPDF2.PdfFileWriter() #creates a blank pdf
for pageNum in range(reader1.numPages): #creates a loop to readr all of the pages and add to a new document
    page = reader1.getPage(pageNum)
    writer.addPage(page)

#does the same thing for 2nd doc
for pageNum in range(readr2.numPages):  # creates a loop to readr all of the pages and add to a new document
        page = readr2.getPage(pageNum)
        writer.addPage(page)

#save the combined doc now.  wb is the write binanry mode argument
outputfile = open('c:\\Git\\CFF\\API\psl.pdf', 'wb')

#write the new file
writer.write(outputfile)

#close the files
outputfile.close()
pdf1File.close()
pdf2File.close()