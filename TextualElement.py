from Run import *
class TextualElement():
    def __init__(self):
        self.lineNumber = 0
        self.headerFooterBody = 0
        self.sectionOfDocument = ""
        self.runs = []

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
    
    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
