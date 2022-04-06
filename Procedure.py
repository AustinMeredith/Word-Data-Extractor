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
    
    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
