from Parser import *
from VariableUtility import *
#using VariableUtility for its intended purpose

vu = VariableUtility()
vu.setOutputFileLocation("C:/Users/marti/Desktop/Word Data Extraction/ParseTests")
vu.setOutputFileName("Matters.xml")
vu.setInputFilePath("C:/Users/marti/Desktop/Word Data Extraction/ParseTests/Assembly Procedure-T1.docx")
Parser = Parser(vu.getInputFilePath())
paragraphList = Parser.paragraphParse()

xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n<WordDoc\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:noNamespaceSchemaLocation=\"DEO3.xsd\">\n"
for element in paragraphList:
    xml += element.XMLReturn(1)
    xml += "\n"
xml +="</WordDoc>"
outputFile = open(vu.getOutputFileLocation() + "\\" + vu.getOutputFileName(), "wt")
outputFile.write(xml)
outputFile.close()
