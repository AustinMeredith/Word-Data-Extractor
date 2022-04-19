#Purpose is to handle the string variables and provide general utilities to the program
import os.path #module handles file paths in the os
class VariableUtility():
    def __init__(self):
        self.OutputFileLocation = ""
        self.OutputFileName = ""
        self.InputFilePath = ""
        self.Illegal = "#%&{}\\<>*?/$!\'\":+`|=@"  #Illegal character set for filenames in Windows

    def getOutputFileLocation(self):
        return self.OutputFileLocation

    def getOutputFileName(self):
        return self.OutputFileName

    def getInputFilePath(self):
        return self.InputFilePath

    def setOutputFileLocation(self, location): #If the OutputFileLocation is a directory then it will be set, otherwise it will be set to an empty string
        self.OutputFileLocation = location
        if(self.OutputCheckValidity()):
            return True
        else:
            self.OutputFileLocation = ""
            return False

    def setOutputFileName(self, name): #If the OutputFileName is a valid name in Windows then it will be set, otherwise it will be set to an empty string
        self.OutputFileName = name
        if(self.OutputNameCheckValidity()):
            return True
        else:
            self.OutputFileName= ""
            return False

    def setInputFilePath(self, path): #If the InputFilePath is a file on the filesystem and ends with '.docx' then it will be set, otherwise it will be set to an empty string
        self.InputFilePath = path
        if(self.InputCheckValidity()):
            return True
        else:
            self.OutputFileName= ""
            return False
    
    def OutputCheckValidity(self): #Checks if OutputFileLocation is valid
        if (os.path.isdir(self.OutputFileLocation)):
            return True
        else:
            return False

    def OutputNameCheckValidity(self): #Checks if OutputFileName is valid
        for x in self.Illegal:
            if (self.OutputFileName.count(x) > 0):
                return False
        return True

    def InputCheckValidity(self): #Checks if InputFilePath is valid
        if (os.path.isfile(self.InputFilePath) and self.InputFilePath.endswith(".docx")):
            return True
        else:
            return False
    def EndProgram(self): #Done by using quit function
        quit()
