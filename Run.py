class Run():
    def __init__(self):
        self.text = ""
        self.bold = False
        self.font = ""
        self.italic = False
        self.style = ""
        self.underline = False

    def getText(self):
        return self.text

    def getBold(self):
        return self.bold

    def getFont(self):
        return self.font

    def getItalic(self):
        return self.italic

    def getStyle(self):
        return self.style

    def getUnderline(self):
        return self.underline

    def setText(self, textArg):
        self.text = textArg

    def setBold(self, boldArg):
        self.bold = boldArg

    def setFont(self, fontArg):
        self.font = fontArg
    
    def setItalic(self, italicArg):
        self.italic = italicArg

    def setStyle(self, styleArg):
        self.style = styleArg

    def setUnderline(self, underlineArg):
        self.underline = underlineArg

    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
