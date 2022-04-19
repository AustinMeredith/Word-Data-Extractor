from Parser import *
from VariableUtility import *
from ProcedureParser import *
from docx2python import docx2python
from docx2python.iterators import enum_at_depth

#using VariableUtility for its intended purpose

vu = VariableUtility()
vu.setOutputFileLocation("C:/Users/marti/Desktop/Word Data Extraction/4-16/Order/OutputXML")
vu.setOutputFileName("Results.xml")
vu.setInputFilePath("C:/Users/marti/Desktop/Word Data Extraction/4-16/Order/TestDocs/Assembly Procedure-T1.docx")
'''Parser = Parser(vu.getInputFilePath())'''

ProcedureParser = ProcedureParser()
Parser = Parser(vu.getInputFilePath())
document = docx2python(vu.getInputFilePath())
docHeader = document.header
docFooter = document.footer
docTables = document.body

docTables = ProcedureParser.removeHeaderOrFooterParagraphs(docTables, docHeader)
docTables = ProcedureParser.removeHeaderOrFooterParagraphs(docTables, docFooter)
docTables = ProcedureParser.removeTabParagraphs(docTables)
docTables = ProcedureParser.removeEmptyParagraphs(docTables)    
structure = ProcedureParser.identifyDocumentStructure(docTables)
tableList = Parser.tablesParse()
paragraphList = Parser.paragraphsParse()
graphicsList = Parser.graphicsParse(vu.getInputFilePath(), vu.getOutputFileLocation())
WordDocList = ProcedureParser.orderByDocumentStructure(paragraphList, graphicsList, paragraphList, structure)

xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n<WordDoc\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:noNamespaceSchemaLocation=\"DEO3.xsd\">\n"
for element in WordDocList:
    xml += element.XMLReturn(1)
    xml += "\n"
xml +="</WordDoc>"
print(xml)
outputFile = open(vu.getOutputFileLocation() + "\\" + vu.getOutputFileName(), "wt")
outputFile.write(xml)
outputFile.close()
