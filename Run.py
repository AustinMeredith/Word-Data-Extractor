#This file was committed by Mason Lanham
class Run():
    def __init__(self, textString, fontString, styleString, boldBool, italicBool, underlineBool):
        self.text = textString
        self.bold = boldBool
        self.font = fontString
        self.italic = italicBool
        self.style = styleString
        self.underline = underlineBool

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

    def appendText(self, textArg):
        self.text += textArg
        
    def XMLReturn(self): #Returns the XML code as a string.
        xml = "<Run"
        xml += " Text=\"" + self.text + "\" Bold=\"" 
        if(self.bold):
            xml += "true"
        else:
            xml += "false"
        xml += "\" Italic=\""
        if(self.italic):
            xml += "true"
        else:
            xml += "false"
        xml += "\" Underline=\""
        if(self.underline):
            xml += "true"
        else:
            xml += "false"
        xml += "\" Font=\"" + self.font
        xml += "\" Style=\"" + self.style + "\"/>"
        return xml
