class GraphicalElement():
    def __init__(self):
        self.lineNumber = 0
        self.headerFooterBody = 0
        self.sectionOfDocument = ""
        self.filePath = ""

    def getLineNumber(self):
        return self.lineNumber

    def getHeaderFooterBody(self):
        return self.headerFooterBody

    def getSectionOfDocument(self):
        return self.sectionOfDocument

    def getFilePath(self):
        return self.filePath

    def setLineNumber(self, lineNumberArg):
        self.lineNumber = lineNumberArg

    def setHeaderFooterBody(self, headerFooterBodyArg):
        self.headerFooterBody = headerFooterBodyArg

    def setSectionOfDocument(self, sectionOfDocumentArg):
        self.sectionOfDocument = sectionOfDocumentArg
    
    def setFilePath(self, filePathArg):
        self.filePath = filePathArg

    def identifyGraphic(self, lineNumber):
        return True

    def extractGraphic(self, lineNumber):
        return True
    
    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
