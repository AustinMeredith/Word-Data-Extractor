from Run import *
class TextualElement():
    def __init__(self, lineInt, hfbInt, sectionString, runsList):
        self.lineNumber = lineInt
        self.headerFooterBody = hfbInt
        self.sectionOfDocument = sectionString
        self.runs = runsList

    def getLineNumber(self):
        return self.lineNumber

    def getHeaderFooterBody(self):
        return self.headerFooterBody

    def getSectionOfDocument(self):
        return self.sectionOfDocument

    def getRuns(self):
        return self.runs

    def setLineNumber(self, lineNumberArg):
        self.lineNumber = lineNumberArg

    def setHeaderFooterBody(self, headerFooterBodyArg):
        self.headerFooterBody = headerFooterBodyArg

    def setSectionOfDocument(self, sectionOfDocumentArg):
        self.sectionOfDocument = sectionOfDocumentArg
    
    def setRuns(self, runsArg):
        self.runs = runsArg

    def appendRun(self, runArg):
        self.runs.append(runArg)

    def identifyText(self, lineNumber):
        return True

    def extractText(self, lineNumber):
        return True
    
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
        xml += "\" SectionOfDocument=\"" + self.sectionOfDocument + "\">"
        for run in self.runs:
            xml += "\n"
            xml += self.indent(indentAmt + 1)
            xml += run.XMLReturn()
        xml += "\n"
        xml += self.indent(indentAmt)
        xml += "</TextualElement>"
        return xml
