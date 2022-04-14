from docx2python.iterators import enum_at_depth
from docx2python.iterators import enum_cells
import re

class ProcedureParser():
    def __init__(self):
        #Tokens1 sublevel of Token0
        self.Tokens0 = []
        self.Tokens1 = []
        self.ProcedureStrings = []
        self.SubProcedureStrings = []
        
    def generateTokens0(self, prePattern, postPattern):
        for x in range(100):
            self.Tokens0.append(prePattern + str(x) + postPattern)

    def generateTokens1(self, prePattern, postPattern):
        for x in range(100):
            self.Tokens1.append(prePattern + str(x) + postPattern)
            
    def checkBeginsToken(self, element, tokens):
        for token in tokens:
            if(element[0:len(token)] == token): #if run begins with token
                return token
        return None
        
    from docx2python.iterators import enum_cells

    def removeEmptyParagraphs(self, tables):
        for (i, j, k), cell in enum_cells(tables):
            tables[i][j][k] = [x for x in cell if x]
            
    def identifyProcedureStrings(self, document):
        for (i, j, k, l), paragraph in enum_at_depth(document, 4):
            checkedToken = self.checkBeginsToken(document[i][j][k][l], self.Tokens0)
            if not(checkedToken is None):
                s = str(document[i][j][k][l])
                s = s.replace(checkedToken, "", 1)
                self.ProcedureStrings.append(s)
            
        for (i, j, k, l), paragraph in enum_at_depth(document, 4):
            checkedToken = self.checkBeginsToken(document[i][j][k][l], self.Tokens1)
            if not(checkedToken is None):
                s = str(document[i][j][k][l])
                s = s.replace(checkedToken, "", 1)
                self.ProcedureStrings.append(s)
        
        '''begin = -1
        end = -1
        index = 0
        while(index < len(WordDocList) and begin == -1):                                            #iterate through the WordDocList until begin found or end of list reached
            if(self.checkBeginsToken(WordDocList[index])):                                          #if textual element begins with token
                begin = index - 1                                                                   #set procedure beginning to that index
                while(not(isinstance(WordDocList[begin], TextualElement) and begin >= 0)):          #checking if there is a previous textual element, if so likely the title of the procedure
                    begin = begin - 1
            index += 1
        if(begin == -1):                                                                            #if no begin was found return False there was no procedure
            return False
        while(index < len(WordDocList) and end == -1):                                              #iterate through the WordDocList until end found
            if(not(self.checkBeginsToken(WordDocList[index]))):                                         #if the TextualElement doesn't begin with a token
                end = index                                                                                 #the end is that TextualElement
            index += 1
        if(end == -1):                                                                              #if no end to the procedure was found it is the end of the document
            end = len(WordDocList)
        self.extractProcedure(WordDocList, begin, end)                                              #extractProcedure with the discovered beginning and end
        return True'''

    def extractProcedure(self, WordDocList, begin, end):
        procedure = Procedure([],"",0,"", 0) #procedure instance
        procedure.setProcedureName(WordDocList[begin].getRuns()[0].getText())
        procedure.setLineNumber(WordDocList[begin].getLineNumber())
        procedure.setSectionOfDocument(WordDocList[begin].getSectionOfDocument())
        procedure.setNumberOfSteps(end - begin)
        for x in range(end - begin): #iterate through the elements that belong to the procedure
            print(WordDocList[begin].getRuns()[0].getText())   
            procedure.appendElement(WordDocList.pop(begin)) #append the element at spot index to the procedure and remove it from the list.
        WordDocList.insert(begin, procedure) #add the procedure to the WordDocList
        return True
