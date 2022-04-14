class GraphicalElement():
    def __init__(self, lineInt, pathString):
        self.lineNumber = lineInt
        self.filePath = pathString

    def getLineNumber(self):
        return self.lineNumber

    def getFilePath(self):
        return self.filePath

    def setLineNumber(self, lineNumberArg):
        self.lineNumber = lineNumberArg

    def setFilePath(self, filePathArg):
        self.filePath = filePathArg

    def indent(self, indentAmt): #Used in XMLReturn returns spaces for indentation
        indentation = ""
        for x in range(indentAmt):
            indentation += "  "
        return indentation

    def XMLReturn(self, indentAmt): #Returns the XML code as a string. Note: indentAmt unused. It's here for the sake of polymorphism.
        xml = self.indent(indentAmt)
        xml += "<GraphicalElement"
        xml += " LineNumber=\"" + str(self.lineNumber)
        xml += "\" FilePath=\"" + self.filePath + "\"/>"
        return xml
