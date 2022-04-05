from TextualElement import *
from GraphicalElement import *

class Cell():
    def __init__(self):
        self.textualElements = []
        self.graphicalElements = []
        self.tableName = ""
        self.column = 0
        self.row = 0

    def getTextualElements(self):
        return self.textualElements

    def getGraphics(self):
        return self.graphicalElements

    def getTableName(self):
        return self.TableName

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def setTextualElement(self, textualArg):
        self.textualElements = textualArg

    def setGraphicalElements(self, graphicsArg):
        self.graphics = graphicsArg

    def setTableName(self, tableNameArg):
        self.tableName = tableNameArg
        
    def setRow(self, rowArg):
        self.row = rowArg

    def setCollumn(self, columnArg):
        self.column = columnArg

    def appendText(self, textualElement):
        self.textualElements.append(textualElement)

    def appendGraphics(self, graphicalElement):
        self.graphicalElements.append(graphicalElements)

    def extractCell(self, lineNumber):
        return True
    
    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
