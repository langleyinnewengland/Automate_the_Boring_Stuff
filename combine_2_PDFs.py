#complete code to combine 2 pdf documents.
import PyPDF2
pdf1File=open('meetingminutes1.pdf', 'rb')
pdf2File=open('meetingminutes2.pdf', 'rb')
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
outputfile = open('combinedminutes.pdf', 'wb')

#write the new file
writer.write(outputfile)

#close the files
outputfile.close()
pdf1File.close()
pdf2File.close()