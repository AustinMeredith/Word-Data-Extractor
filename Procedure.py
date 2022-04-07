from TextualElement import *
from GraphicalElement import *

class Procedure():
    def __init__(self, stepList, graphicsList, nameString, lineInt, sectionString, numStepsInt):
        self.steps = stepList
        self.graphics = graphicsList
        self.procedureName = nameString
        self.lineNumber = lineInt
        self.sectionOfDocument = sectionString
        self.numberOfSteps = numStepsInt

    def getSteps(self):
        return self.steps

    def getGraphics(self):
        return self.graphics

    def getProcedureName(self):
        return self.procedureName
    
    def getLineNumber(self):
        return self.lineNumber

    def getSectionOfDocument(self):
        return self.sectionOfDocument

    def getNumberOfSteps(self):
        return self.numberOfSteps

    def setSteps(self, stepsArg):
        self.steps = stepsArg

    def setGraphics(self, graphicsArg):
        self.graphics = graphicsArg

    def setProcedureName(self, procedureNameArg):
        self.procedureName = procedureNameArg
        
    def setLineNumber(self, lineNumberArg):
        self.lineNumber = lineNumberArg

    def setSectionOfDocument(self, sectionOfDocumentArg):
        self.sectionOfDocument = sectionOfDocumentArg

    def setNumberOfSteps(self, numberOfStepsArg):
        self.numberOfSteps = numberOfStepsArg
    
    def identifyProcedure(self, lineNumber):
        return True

    def extractProcedure(self, lineNumber):
        return True

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
        for text in self.steps:
            xml += "\n"
            xml += text.XMLReturn(indentAmt + 1)
        for graphic in self.graphics:
            xml += "\n"
            xml += graphic.XMLReturn(indentAmt + 1)
        xml += "\n"
        xml += self.indent(indentAmt)
        xml += "</Procedure>"
        return xml
