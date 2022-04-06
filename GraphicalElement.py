class GraphicalElement():
    def __init__(self, lineInt, hfbInt, sectionString, pathString):
        self.lineNumber = lineInt
        self.headerFooterBody = hfbInt
        self.sectionOfDocument = sectionString
        self.filePath = pathString

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
    
    def XMLReturn(self): #Returns the XML code as a string
        xml = "<GraphicalElement"
        xml += " LineNumber=\"" + str(self.lineNumber)
        xml += "\" HeaderFooterBody=\"" + str(self.headerFooterBody)  
        xml += "\" SectionOfDocument=\"" + self.sectionOfDocument
        xml += "\" FilePath=\"" + self.filePath + "\"/>"
        return xml
