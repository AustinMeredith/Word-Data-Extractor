from Parser import *
from VariableUtility import *
from ProcedureParser import *
from docx2python import docx2python
from docx2python.iterators import enum_at_depth

#using VariableUtility for its intended purpose

vu = VariableUtility()
vu.setOutputFileLocation("C:/Users/marti/Desktop/Word Data Extraction/4-20/OutputXML")
vu.setOutputFileName("Results.xml")
vu.setInputFilePath("C:/Users/marti/Desktop/Word Data Extraction/4-20/Test Docs/MyTest.docx")
Parser = Parser(vu.getInputFilePath())
ProcedureParser = ProcedureParser()
ProcedureParser.generateTokens0("", ")\t")
ProcedureParser.generateTokens1("\t", ")\t\t")
#ProcedureParser.generateTokens0("", ".   ")
document = docx2python(vu.getInputFilePath())
docHeader = document.header
docFooter = document.footer
docTables = document.body
docTables = ProcedureParser.removeHeaderOrFooterParagraphs(docTables, docHeader)
docTables = ProcedureParser.removeHeaderOrFooterParagraphs(docTables, docFooter)
docTables = ProcedureParser.removeTabParagraphs(docTables)
docTables = ProcedureParser.removeEmptyParagraphs(docTables)    
structure = ProcedureParser.identifyDocumentStructure(docTables)
ProcedureStringList = ProcedureParser.identifyProcedureStrings(docTables)
tableList = Parser.tablesParse()
paragraphList = Parser.paragraphsParse()
graphicsList = Parser.graphicsParse(vu.getInputFilePath(), vu.getOutputFileLocation())
WordDocList = tableList + paragraphList + graphicsList
WordDocList = ProcedureParser.orderByDocumentStructure(paragraphList, graphicsList, tableList, structure)
ProcedureParser.identifyProcedure(WordDocList, ProcedureStringList[0], ProcedureStringList[1])

xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n<WordDoc\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:noNamespaceSchemaLocation=\"DEO3.xsd\">\n"
for element in WordDocList:
    xml += element.XMLReturn(1)
    xml += "\n"
xml +="</WordDoc>"
print(xml)
outputFile = open(vu.getOutputFileLocation() + "\\" + vu.getOutputFileName(), "wt")
outputFile.write(xml)
outputFile.close()
