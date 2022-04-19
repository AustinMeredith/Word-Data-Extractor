from Parser import *
from VariableUtility import *
#using VariableUtility for its intended purpose

vu = VariableUtility()
vu.setOutputFileLocation("C:/Users/marti/Desktop/Word Data Extraction/4-16/Order/OutputXML")
vu.setOutputFileName("Results1.xml")
vu.setInputFilePath("C:/Users/marti/Desktop/Word Data Extraction/4-16/Order/TestDocs/Assembly Procedure-T1.docx")
Parser = Parser(vu.getInputFilePath())

tableList = Parser.tablesParse()
paragraphList = Parser.paragraphsParse()
graphicsList = Parser.graphicsParse(vu.getInputFilePath(), vu.getOutputFileLocation())

WordDocList = paragraphList + graphicsList + tableList
structure = []

for element in WordDocList:
    if(isinstance(element, TextualElement)):
        runText = ""
        for run in element.getRuns():
            runText += run.getText()
        print(runText[0:80])
        structure.append("x")
    elif(isinstance(element, GraphicalElement)):
        structure.append("i")
    else:
        structure.append("t")

print(structure)
print(len(structure))
'''xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n<WordDoc\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:noNamespaceSchemaLocation=\"DEO3.xsd\">\n"
for element in WordDocList:
    xml += element.XMLReturn(1)
    xml += "\n"
xml +="</WordDoc>"
print(xml)'''
'''outputFile = open(vu.getOutputFileLocation() + "\\" + vu.getOutputFileName(), "wt")
outputFile.write(xml)
outputFile.close()'''
