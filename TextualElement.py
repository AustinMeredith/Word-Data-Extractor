#This file was committed by Mason Lanham
from Run import *
class TextualElement():
    def __init__(self, lineInt, hfbInt, styleString, runsList):
        self.lineNumber = lineInt
        self.headerFooterBody = hfbInt
        self.style = styleString
        self.runs = runsList

    def getLineNumber(self):
        return self.lineNumber

    def getHeaderFooterBody(self):
        return self.headerFooterBody

    def getStyle(self):
        return self.style

    def getRuns(self):
        return self.runs

    def getRun(self, index):
        if index > -1 and index < len(self.runs):
            return self.runs[index]
        else:
            return None

    def getRunsText(self):
        runText = ""
        for run in self.runs:
            runText += run.getText()
        return runText
        

    def setLineNumber(self, lineNumberArg):
        self.lineNumber = lineNumberArg

    def setHeaderFooterBody(self, headerFooterBodyArg):
        self.headerFooterBody = headerFooterBodyArg

    def setStyle(self, styleArg):
        self.style = styleArg
    
    def setRuns(self, runsArg):
        self.runs = runsArg

    def appendRun(self, runArg):
        self.runs.append(runArg)
    
    def indent(self, indentAmt): #Used in XMLReturn returns spaces for indentation
        indentation = ""
        for x in range(indentAmt):
            indentation += "  "
        return indentation
    
    def XMLReturn(self, indentAmt): #Returns the XML code for this object as a string
        xml = self.indent(indentAmt)
        xml += "<TextualElement"
        xml += " LineNumber=\"" + str(self.lineNumber)
        xml += "\" HeaderFooterBody=\"" + str(self.headerFooterBody)
        xml += "\" Style=\"" + self.style + "\">"
        for run in self.runs:
            xml += "\n"
            xml += self.indent(indentAmt + 1)
            xml += run.XMLReturn()
        xml += "\n"
        xml += self.indent(indentAmt)
        xml += "</TextualElement>"
        return xml
