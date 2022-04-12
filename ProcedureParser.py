from Procedure import *
import re

class ProcedureParser():
    def __init__(self):
        self.tokens = []
        
    def generateTokens(self):
        #Procedurally generating tokens: "1.","2.","3."..."100."
        for x in range(100):
            self.tokens.append(str(x) + ".")
    
    def checkBeginsToken(self, element):
        if isinstance(element, TextualElement): #if element is a TextualElement
            for token in self.tokens: #iterate through the tokens
                if not(re.search("^" + token, element.getRuns()[0].getText()) is None): #if run begins with token
                    return True
                        
    def identifyProcedure(self, WordDocList):
        begin = -1
        end = -1
        index = 0
        while(index < len(WordDocList) and begin == -1):                                            #iterate through the WordDocList until begin found or end of list reached
            if(self.checkBeginsToken(WordDocList[index])):                                          #if textual element begins with token
                begin = index                                                                       #set procedure beginning to that index
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
        return True

    def extractProcedure(self, WordDocList, begin, end):
        procedure = Procedure([],"",0,"", 0) #procedure instance
        procedure.setProcedureName(WordDocList[begin].getRuns()[0].getText())
        procedure.setLineNumber(WordDocList[begin].getLineNumber())
        procedure.setSectionOfDocument(WordDocList[begin].getSectionOfDocument())
        procedure.setNumberOfSteps(end - begin)
        index = begin #beginning of the procedure
        while index < end: #iterate through the elements that belong to the procedure
            procedure.appendElement(WordDocList.pop(index)) #append the element at spot index to the procedure and remove it from the list.
            index += 1
        WordDocList.insert(begin, procedure) #add the procedure to the WordDocList
        return True
