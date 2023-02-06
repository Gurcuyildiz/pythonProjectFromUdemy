

'''

  There are many libraries in Python for working with PDFs,
   each with their pros and cons, the most common one being PyPDF2.
   You can install it with (note the case-sensitivity,
   you need to make sure your capitilization matches):

pip install PyPDF2

Keep in mind that not every PDF file can be read with this library.
PDFs that are too blurry, have a special encoding, encrypted,
 or maybe just created with a particular program that doesn't work well with PyPDF2 won't be able to be read. If you find yourself in this situation, try using the libraries linked above, but keep in mind, these may also not work. The reason for this is because of the many different parameters for a PDF and how non-standard the settings can be, text could be shown as an image instead of a utf-8 encoding. There are many parameters to consider in this aspect.

As far as PyPDF2 is concerned, it can only read the text from a PDF document,
 it won't be able to grab images or other media files from a PDF. ___

Working with PyPDF2
Let's being showing the basics of the PyPDF2 library.

# note the capitalization
import PyPDF2
Reading PDFs
Similar to the csv library, we open a pdf, then create a reader object for it.
Notice how we use the binary method of reading , 'rb', instead of just 'r'.

# Notice we read it as a binary with 'rb'
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
pdf_reader.numPages
5
page_one = pdf_reader.getPage(0)
We can then extract the text:

page_one_text = page_one.extractText()
page_one_text
'''

# import PyPDF2
# #open the pdf file, read binary = rb
# f = open('Working_Business_Proposal.pdf','rb')
# #we attached a reader file by passing the file
# pdf_reader = PyPDF2.PdfFileReader(f)
# #shows many pages are there
# pdf_reader.numPages
# 5
# #first page
# page_one = pdf_reader.getPage(0)
# We can then extract the text:
# #view the first page text
# page_one_text
#f.close()#close the file

#if you get blank then it means your pdf is not compatible with that library, try another library


'''
 Adding to PDFs
We can not write to PDFs using Python because of the differences between the single string type of Python,
 and the variety of fonts, placements, and other parameters that a PDF could have.

What we can do is copy pages and append pages to the end.
'''


# f = open('Working_Business_Proposal.pdf','rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# first_page = pdf_reader.getPage(0)# a specific first page object
#creating a writer object
# pdf_writer = PyPDF2.PdfFileWriter()
#adding the page
# pdf_writer.addPage(first_page)
#open a new file  with write binary mode
# pdf_output = open("Some_New_Doc.pdf","wb")
#
# pdf_writer.write(pdf_output)
# f.close()
#pdf_output.close()


'''
 Simple Example
Let's try to grab all the text from this PDF file:
'''
# f = open('Working_Business_Proposal.pdf', 'rb')
#
# # List of every page's text.
# # The index will correspond to the page number.
# pdf_text = []
# #creading our reader object passing our file we opened
# pdf_reader = PyPDF2.PdfFileReader(f)
#
# for p in range(pdf_reader.numPages):
#     page = pdf_reader.getPage(p)
#
#     #will extract the text of the page and append to pdf text
#     pdf_text.append(page.extractText())
#
# pdf_text
# print(pdf_text[3])


#how to find all matches in regular expresion in python