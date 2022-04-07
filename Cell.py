from TextualElement import *
from GraphicalElement import *

class Cell():
    def __init__(self, textList, graphicsList, tableString, columnInt, rowInt):
        self.textualElements = textList
        self.graphicalElements = graphicsList
        self.tableName = tableString
        self.column = columnInt
        self.row = rowInt

    def getTextualElements(self):
        return self.textualElements

    def getGraphicalElements(self):
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
    
    def indent(self, indentAmt): #Used in XMLReturn returns spaces for indentation
        indentation = ""
        for x in range(indentAmt):
            indentation += "  "
        return indentation
    
    def XMLReturn(self, indentAmt): #Returns the XML Code for this object as a string
        xml = ""
        xml += self.indent(indentAmt)
        xml += "<Cell"
        xml += " Row=\"" + str(self.row)
        xml += "\" Column=\"" + str(self.column)
        xml += "\" Table=\"" + self.tableName + "\">"
        for text in self.textualElements:
            xml += "\n"
            xml += text.XMLReturn(indentAmt + 1)
        for graphic in self.graphicalElements:
            xml += "\n"
            xml += graphic.XMLReturn(indentAmt + 1)
        xml += "\n"
        xml += self.indent(indentAmt)
        xml += "</Cell>"
        return xml
