from TextualElement import *
from GraphicalElement import *


class Procedure():
    def __init__(self, elementList, nameString, lineInt, sectionString, numStepsInt):
        self.elements = elementList
        self.procedureName = nameString
        self.lineNumber = lineInt
        self.sectionOfDocument = sectionString
        self.numberOfSteps = numStepsInt
            
    def getElements(self):
        return self.elements

    def getProcedureName(self):
        return self.procedureName
    
    def getLineNumber(self):
        return self.lineNumber

    def getSectionOfDocument(self):
        return self.sectionOfDocument

    def getNumberOfSteps(self):
        return self.numberOfSteps

    def setElements(self, elementsArg):
        self.elements = elementsArg

    def setProcedureName(self, procedureNameArg):
        self.procedureName = procedureNameArg
        
    def setLineNumber(self, lineNumberArg):
        self.lineNumber = lineNumberArg

    def setSectionOfDocument(self, sectionOfDocumentArg):
        self.sectionOfDocument = sectionOfDocumentArg

    def setNumberOfSteps(self, numberOfStepsArg):
        self.numberOfSteps = numberOfStepsArg

    def appendElement(self, elementArg):
        self.elements.append(elementArg)

    def indent(self, indentAmt): #Used in XMLReturn returns spaces for indentation
        indentation = ""
        for x in range(indentAmt):
            indentation += "  "
        return indentation
    
    def XMLReturn(self, indentAmt): #Returns the XML Code for this object as a string
        xml = ""
        xml += self.indent(indentAmt)
        xml += "<Procedure"
        xml += " ProcedureName=\"" + self.procedureName
        xml += "\" LineNumber=\"" + str(self.lineNumber)
        xml += "\" SectionOfDocument=\"" + self.sectionOfDocument
        xml += "\" NumberOfSteps=\"" + str(self.numberOfSteps) + "\">"
        for element in self.elements:
            xml += "\n"
            xml += element.XMLReturn(indentAmt + 1)
        xml += "\n"
        xml += self.indent(indentAmt)
        xml += "</Procedure>"
        return xml
