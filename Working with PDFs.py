#This will explain how to use PyPDF2 to interact with pypdf2.  It does need to be installed

#import package
import PyPDF2

#to change the working directory
import os
#returns current directory
os.getcwd()

#change directory
#os.chdir('c:\\xxxxx')

#opem a file.  'rb opens in read binary mode
pdfFile=open('meetingminutes1.pdf', 'rb')

#read the pdfile
reader=PyPDF2.PdfFileReader(pdfFile)
#number of pages
reader.numPages

#get a page and extract text
page = reader.getPage(0)
page.extractText

#get all the text in the document
for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

