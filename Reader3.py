#Purpose is to see if I could extract the text from a document I manually edited, then save in a .txt
import lxml
from docx import Document

doc = Document('Test.docx')
new = open("New.txt","w")
for paragraph in doc.paragraphs:
    new.write(paragraph.text)
new.close()
'''References:
https://www.geeksforgeeks.org/reading-writing-text-files-python/
https://python-docx.readthedocs.io/en/latest/api/text.html#paragraph-objects
https://www.w3schools.com/xml/schema_intro.asp
https://lxml.de/tutorial.html'''
