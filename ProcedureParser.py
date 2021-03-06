#This file was committed by Mason Lanham

#Note 1 There is a problem regarding hyperlinks in that Python-docx can't see hyperlinks at all, so when parsing the document with the Parser class (which uses Python-docx) those hyperlinks are invisible,
#and thus aren't recorded as textual elements. That's why it's necessary to remove hyperlinks from the document.
#Note 2 Text boxes, whether integrated into the text, or as inline shapes, python-docx can't detect those text boxes, and thus they aren't recorded as textual elements. Thus, it's necessary to remove text boxes.
#Note 3 Certain characters that can appear in Word are not compatable with the encoding of the XML output (UTF-8), and thus must be removed.

from docx2python.iterators import enum_at_depth
from docx2python.iterators import enum_cells
from TextualElement import *
from Procedure import *
from Table import *

class ProcedureParser():
    def __init__(self):
        self.Tokens0 = []
        self.Tokens1 = []
        self.Resets0 = []
        self.Resets1 = []
        self.Token0Index = -1
        self.Token1Index = -1
        
    def generateTokens0(self, prePattern, postPattern, numberingType): #Method generates the tokens that are used to identify procedures
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        romanNumeral = ["i", "ii", "iii", "iv", "v" , "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv"]
        if(numberingType == 0):
            for x in range(1, 25):
                self.Tokens0.append(prePattern + str(x) + postPattern)
        elif(numberingType == 1):
            for x in range(0, 25):
                self.Tokens0.append(prePattern + str(lowercase[x]) + postPattern)
        elif(numberingType == 2):
            for x in range(0, 25):
                self.Tokens0.append(prePattern + str(lowercase[x].upper()) + postPattern)
        elif(numberingType == 3):
            for x in range(0, 25):
                self.Tokens0.append(prePattern + str(romanNumeral[x]) + postPattern)
        elif(numberingType == 4):
            for x in range(0, 25):
                self.Tokens0.append(prePattern + str(romanNumeral[x].upper()) + postPattern)
        else:
            for x in range(1, 25):
                self.Tokens0.append(prePattern + str(x) + postPattern)
                
    def generateTokens1(self, prePattern, postPattern, numberingType): #Method generates the tokens that are used to identify sub-procedures
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        romanNumeral = ["i", "ii", "iii", "iv", "v" , "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiv", "xxv"]
        if(numberingType == 0):
            for x in range(1, 25):
                self.Tokens1.append(prePattern + str(x) + postPattern)
        elif(numberingType == 1):
            for x in range(0, 25):
                self.Tokens1.append(prePattern + str(lowercase[x]) + postPattern)
        elif(numberingType == 2):
            for x in range(0, 25):
                self.Tokens1.append(prePattern + str(lowercase[x].upper()) + postPattern)
        elif(numberingType == 3):
            for x in range(0, 25):
                self.Tokens1.append(prePattern + str(romanNumeral[x]) + postPattern)
        elif(numberingType == 4):
            for x in range(0, 25):
                self.Tokens1.append(prePattern + str(romanNumeral[x].upper()) + postPattern)
        else:
            for x in range(1, 25):
                self.Tokens0.append(prePattern + str(x) + postPattern)
    
    def identifyDocumentStructure(self, docTables): #Method identifies the Word document structure from the 4-dimenstional array given by docx2python
        structure = []
        for element0 in docTables:
            if(len(element0) > 1):
                structure.append("t")
            else:
                for element3 in element0[0][0]:
                    if "----media/image" in element3:
                        structure.append("i")
                    elif(len(element3) > 0):
                        structure.append("x")
        return structure

    def identifyInternalDocumentStructure(self, WordDocList): #Method identifies the internal structure of the WordDocList array of objects
        structure = []
        for element in WordDocList:
            if(isinstance(element, TextualElement)):
                structure.append("x")
            elif(isinstance(element, GraphicalElement)):
                structure.append("i")
            else:
                structure.append("t")
        return structure

    def orderByDocumentStructure(self, TextList, GraphicsList, TableList, structure): #Method reorders the WordDocList array of objects to match the Word document structure identified in identifyDocumentStructure(docTables) method.
        orderedWordDocList = []
        iteration = 0
        for part in structure:
            if part == 'x':
                orderedWordDocList.append(TextList.pop(0))
            elif part == 'i':
                orderedWordDocList.append(GraphicsList.pop(0))
            else:
                orderedWordDocList.append(TableList.pop(0))
            orderedWordDocList[iteration].setLineNumber(iteration)
            iteration += 1
        return orderedWordDocList
    
    def removeHeaderOrFooterParagraphs(self, docTables, docHeaderOrFooter): #Method removes header and footer paragraphs from the 4-dimenstional array given by docx2python
        for (i, j, k, l), paragraph in enum_at_depth(docTables, 4):
            for (i, j, k, l), paragraph in enum_at_depth(docHeaderOrFooter, 4):
                if docTables[i][j][k][l] == docHeaderOrFooter[i][j][k][l]:
                    docTables[i][j][k][l] == ""
        return docTables

    def removeEmptyParagraphs(self, docTables): #Method removes empty paragraphs from the 4-dimenstional array given by docx2python
        for (i, j, k), cell in enum_cells(docTables):
            docTables[i][j][k] = [x for x in cell if x]
        return docTables

    def removeTabParagraphs(self, docTables): #Method removes tab paragraphs (paragraphs composed of tabs) from the 4-dimenstional array given by docx2python
        for (i, j, k, l), paragraph in enum_at_depth(docTables, 4):
            if docTables[i][j][k][l] == "\t" or docTables[i][j][k][l] == "\t\t":
                docTables[i][j][k][l] = ""
        return docTables
                        
    def checkBeginsToken0(self, element, tokens): #Method checks if the element begins with a procedure token
        index = 0
        for token in tokens:
            if(element[0:len(token)] == token):
                self.Token0Index = index
                return token
            index += 1
        return None

    def checkBeginsToken1(self, element, tokens): #Method checks if the element begins with a sub-procedure token
        index = 0
        for token in tokens:
            if(element[0:len(token)] == token):
                self.Token1Index = index
                return token
            index += 1
        return None
    
    def identifyProcedureStrings(self, document): #Method identifies procedure strings and sub-procedure strings in the 4-dimenstional array given by docx2python
        ProcedureStrings = []
        SubProcedureStrings = []
        resetIndex = 0
        for (i, j, k, l), paragraph in enum_at_depth(document, 4):
            checkedToken = self.checkBeginsToken0(document[i][j][k][l], self.Tokens0)
            if not(checkedToken is None) and checkedToken == self.Tokens0[self.Token0Index]:
                s = str(document[i][j][k][l])
                s = s.replace(checkedToken, "", 1)
                ProcedureStrings.append(s)
                resetIndex += 1
                if len(self.Tokens1) > 0:
                    SubProcedureStrings = SubProcedureStrings + self.identifySubProcedureStrings(document, i, j, k, l + 1)

            if not(checkedToken is None) and self.Token0Index < resetIndex:
                self.Resets0.append(resetIndex)
                resetIndex = 0
            
        self.Token0Index = -1
        self.Token1Index = -1
        return[ProcedureStrings, SubProcedureStrings]
    
    def identifySubProcedureStrings(self, document, i, j, k, l): #Method identifies sub-procedure strings in the 4-dimenstional array given by docx2python
        SubProcedureStrings = []
        resetIndex = 0
        while l < len(document[i][j][k]):
            checkedToken = self.checkBeginsToken1(document[i][j][k][l], self.Tokens1)
            if self.isSubProcedureString(document[i][j][k][l]):
                s = str(document[i][j][k][l])
                s = s.replace(checkedToken, "", 1)
                SubProcedureStrings.append(s)
                resetIndex += 1
            if l == len(document[i][j][k]) - 1:
                self.Resets1.append(resetIndex)
            checkedToken = self.checkBeginsToken0(document[i][j][k][l], self.Tokens0)
            if (not(checkedToken is None) and checkedToken == self.Tokens0[self.Token0Index]):
                self.Resets1.append(resetIndex)
                break
            l += 1
        self.Tokens1Index = -1
        return SubProcedureStrings

    def identifyTableProcedureStrings(self, document): #Method identifies procedure strings in the 4-dimenstional array given by docx2python
        ProcedureStrings = []
        for (i, j, k, l), paragraph in enum_at_depth(document, 4):
            checkedToken = self.checkBeginsToken0(document[i][j][k][l], self.Tokens0)
            if not(checkedToken is None) and checkedToken == self.Tokens0[self.Token0Index]:
                s = str(document[i][j][k][l])
                s = s.replace(checkedToken, "", 1)
                ProcedureStrings.append(s)
            elif not(checkedToken is None) and checkedToken != self.Tokens0[self.Token0Index]:
                break
        self.Tokens0Index = -1
        return ProcedureStrings

    def identifyTableProcedure(self, WordDocList, ProcedureStrings): #Method identifies and extract procedures contained within tables in the WordDocList array of objects
        begin = -1
        end = -1
        lastProcedureStringIndex = -1
        index = 0
        if len(ProcedureStrings) > 0:
            while index < len(WordDocList) and begin == -1:
                if(isinstance(WordDocList[index], Table) and not(WordDocList[index].getProcedureParsed())):
                    WordDocList[index].setProcedureParsed()
                    table = WordDocList[index]
                    jndex = 0
                    while jndex < len(WordDocList[index].getCells()) and begin == -1:
                        if len(WordDocList[index].getCells()[jndex].getTextualElements()) > 0 and WordDocList[index].getCells()[jndex].getTextualElements()[0].getRunsText() == ProcedureStrings[0]:
                            begin = jndex
                            end = jndex + table.getNumberOfColumns()
                        jndex += 1
                    while jndex < len(WordDocList[index].getCells()):
                        if len(WordDocList[index].getCells()[jndex].getTextualElements()) > 0 and self.indexProcedureString(WordDocList[index].getCells()[jndex].getTextualElements()[0].getRunsText(), ProcedureStrings) > -1:
                            end = jndex + table.getNumberOfColumns()
                            lastProcedureStringIndex = self.indexProcedureString(WordDocList[index].getCells()[jndex].getTextualElements()[0].getRunsText(), ProcedureStrings)
                        jndex += 1
                index += 1
            if(begin > -1 and end > -1):
                self.extractTableProcedure(WordDocList, begin, end, index - 1, len(ProcedureStrings))
                self.removeFoundProcedureStrings(lastProcedureStringIndex, ProcedureStrings)
                return True
            else:
                return False
        else:
            return False

    def indexProcedureString(self, string, ProcedureStrings): #Method used by identifyTableProcedure(WordDocList, String[]) to identify the index in the procedure string list a particular string is at.
        for x in range(len(ProcedureStrings) - 1):
            if string == ProcedureStrings[x]:
                return x
        return -1

    def removeFoundProcedureStrings(self, index, ProcedureStrings): #Method used by identifyTableProcedure(WordDocList, String[]) to remove the procedure strings that have already been found from the procedure string list
        for x in range(index + 1):
            ProcedureStrings.pop(0)
            
    def extractTableProcedure(self, WordDocList, begin, end, index, steps): #Method to extract the cells of a particular procedure contained within a table and append that to the WordDocList array of objects
        procedure = Procedure([],"",0, 0) #procedure instance
        procedure.setProcedureName(WordDocList[index].getCells()[begin].getTextualElements()[0].getRunsText())
        procedure.setLineNumber(WordDocList[index].getLineNumber())
        procedure.setNumberOfSteps(steps)
        for x in range(begin, end): #iterate through the objects that belong to the procedure 
            procedure.appendElement(WordDocList[index].getCells()[x]) #append the object at spot index to the procedure and remove it from the list.
        WordDocList.insert(index + 1, procedure) #add the procedure to the WordDocList
        return True
    
    def isSubProcedureString(self, string): #Method identifies if a particular string is a sub-procedure string
        checkedToken = self.checkBeginsToken1(string, self.Tokens1)
        if not(checkedToken is None) and checkedToken != self.Tokens0[self.Token0Index] and checkedToken == self.Tokens1[self.Token1Index]:
            return True
        else:
            return False
        
    def identifyProcedure(self, WordDocList, ProcedureStrings, SubProcedureStrings): #Method identifies and extracts procedures
        begin = -1
        end = -1
        index = 0
        Resets1Index = 0
        x = 0
        while x < len(self.Resets0):
            while(index < len(WordDocList) and len(ProcedureStrings) > 0):
                if isinstance(WordDocList[index], TextualElement) and WordDocList[index].getRunsText() == ProcedureStrings[0]:
                    begin = index
                    Resets1Index = 0
                    y = 0
                    while(index < len(WordDocList) and y < self.Resets0[x]):
                        if isinstance(WordDocList[index], TextualElement) and bool(ProcedureStrings) and WordDocList[index].getRunsText() == ProcedureStrings[0]:
                            ProcedureStrings.pop(0)
                            y += 1
                            z = 0
                            while(index < len(WordDocList) and bool(self.Resets1) and z < self.Resets1[Resets1Index]):
                                if isinstance(WordDocList[index], TextualElement) and WordDocList[index].getRunsText() == SubProcedureStrings[0]:
                                    SubProcedureStrings.pop(0)
                                    z += 1
                                index += 1
                        index += 1
                        Resets1Index += 1
                    index = index - 1
                    end = index
                    index = self.extractProcedure(WordDocList, begin, end)
                elif (isinstance(WordDocList[index], Table)):
                    self.identifyTableProcedure(WordDocList, ProcedureStrings)
                index += 1
            x += 1
        
    def extractProcedure(self, WordDocList, begin, end): #Method extracts the objects that make up a procedure of TextualElements (can include other elements as well)
        procedure = Procedure([],"",0, 0) #procedure instance
        procedure.setProcedureName(WordDocList[begin].getRuns()[0].getText())
        procedure.setLineNumber(WordDocList[begin].getLineNumber())
        procedure.setNumberOfSteps(end - begin)
        for x in range(end - begin): #iterate through the objects that belong to the procedure 
            procedure.appendElement(WordDocList.pop(begin)) #append the object at spot index to the procedure and remove it from the list.
        WordDocList.insert(begin, procedure) #add the procedure to the WordDocList
        return begin
