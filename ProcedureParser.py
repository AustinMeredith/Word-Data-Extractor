#Note 1 the removeHyperLinks method removes the tags surrounding hyperlinks in the list provided by docx2pyton.document.body, but leaves the text that the hyperlink was associated with.
#The problem lies in that python-docx can't see hyperlinks at all, so when parsing the document with the Parser class (which uses python-docx) those hyperlinks are invisible, and thus aren't recorded as textual elements.
#That's why it's necessary to remove hyperlinks.
#Note 2 Text boxes, whether integrated into the text, or as inline shapes, python-docx can't detect those text boxes, and thus they aren't recorded as textual elements. Thus, it's necessary to remove text boxes.
#Note 3 Certain characters that appear in Word are not compatable with the encoding of the XML output (UTF-8), and thus must be removed.
#Note 4 I know that many of these methods could be significantly optimized compared to their current state, but time crunch meant I just had to make it functional.
from docx2python.iterators import enum_at_depth
from docx2python.iterators import enum_cells
from TextualElement import *
from Procedure import *
from Table import *

class ProcedureParser():
    def __init__(self):
        #Tokens1 sublevel of Token0
        self.Tokens0 = []
        self.Tokens1 = []
        self.Resets0 = []
        self.Resets1 = []
        self.Token0Index = -1
        self.Token1Index = -1
        
    def generateTokens0(self, prePattern, postPattern):
        for x in range(1, 100):
            self.Tokens0.append(prePattern + str(x) + postPattern)
        self.Token0 = self.Tokens0[0]

    def generateTokens1(self, prePattern, postPattern):
        for x in range(1, 100):
            self.Tokens1.append(prePattern + str(x) + postPattern)
        self.Token1 = self.Tokens1[0]
            
    def checkBeginsToken0(self, element, tokens):
        index = 0
        for token in tokens:
            if(element[0:len(token)] == token): #if run begins with token
                self.Token0Index = index
                return token
            index += 1
        return None

    def checkBeginsToken1(self, element, tokens):
        index = 0
        for token in tokens:
            if(element[0:len(token)] == token): #if run begins with token
                self.Token1Index = index
                return token
            index += 1
        return None
    
    def identifyDocumentStructure(self, docTables):
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

    def identifyInternalDocumentStructure(self, WordDocList):
        structure = []
        for element in WordDocList:
            if(isinstance(element, TextualElement)):
                structure.append("x")
            elif(isinstance(element, GraphicalElement)):
                structure.append("i")
            else:
                structure.append("t")
        return structure

    def orderByDocumentStructure(self, TextList, GraphicsList, TableList, structure):
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
    
    def removeHeaderOrFooterParagraphs(self, docTables, docHeaderOrFooter):
        for (i, j, k, l), paragraph in enum_at_depth(docTables, 4):
            for (i, j, k, l), paragraph in enum_at_depth(docHeaderOrFooter, 4):
                if docTables[i][j][k][l] == docHeaderOrFooter[i][j][k][l]:
                    docTables[i][j][k][l] == ""
        return docTables

    def removeEmptyParagraphs(self, docTables):
        for (i, j, k), cell in enum_cells(docTables):
            docTables[i][j][k] = [x for x in cell if x]
        return docTables

    def removeTabParagraphs(self, docTables):
        for (i, j, k, l), paragraph in enum_at_depth(docTables, 4):
            if docTables[i][j][k][l] == "\t" or docTables[i][j][k][l] == "\t\t":
                docTables[i][j][k][l] = ""
        return docTables
                
    def findSubstringLocation(self, string, substring):
        for x in range(len(string) - len(substring) + 1):
            if string[x:x + len(substring)] == substring:
                return x
        return -1
        
    def removeHyperLinks(self, docTables): #removes the hyperlink tags, but not the text itself. See Note 1
        begin = 0
        end = 0
        for (i, j, k, l), paragraph in enum_at_depth(docTables, 4):
            if ("<a href=" in docTables[i][j][k][l]) and ("</a>" in docTables[i][j][k][l]):
                begin = self.findSubstringLocation(docTables[i][j][k][l], "<a href=")
                end = self.findSubstringLocation(docTables[i][j][k][l], "\">")
                docTables[i][j][k][l] = (docTables[i][j][k][l][0:begin] + docTables[i][j][k][l][end + 2: len(docTables[i][j][k][l])]).replace("</a>", "")
        return docTables

    def getTokenIndex(self, token, tokenList):
        index = 0
        for t in tokenList:
            if t == token:
                return index
            index += 1
        return -1
    
    def identifyProcedureStrings(self, document):
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
    
    def identifySubProcedureStrings(self, document, i, j, k, l):
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

    def identifyTableProcedureStrings(self, document):
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

    def identifyTableProcedure(self, WordDocList, ProcedureStrings):
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

    def indexProcedureString(self, string, ProcedureStrings):
        for x in range(len(ProcedureStrings) - 1):
            if string == ProcedureStrings[x]:
                return x
        return -1

    def removeFoundProcedureStrings(self, index, ProcedureStrings):
        for x in range(index + 1):
            ProcedureStrings.pop(0)
            
    def extractTableProcedure(self, WordDocList, begin, end, index, steps):
        procedure = Procedure([],"",0, 0) #procedure instance
        procedure.setProcedureName(WordDocList[index].getCells()[begin].getTextualElements()[0].getRunsText())
        procedure.setLineNumber(WordDocList[index].getLineNumber())
        procedure.setNumberOfSteps(steps)
        for x in range(begin, end): #iterate through the elements that belong to the procedure 
            procedure.appendElement(WordDocList[index].getCells()[x]) #append the element at spot index to the procedure and remove it from the list.
        WordDocList.insert(index + 1, procedure) #add the procedure to the WordDocList
        return True
    
    def isSubProcedureString(self, string):
        checkedToken = self.checkBeginsToken1(string, self.Tokens1)
        if not(checkedToken is None) and checkedToken != self.Tokens0[self.Token0Index] and checkedToken == self.Tokens1[self.Token1Index]:
            return True
        else:
            return False
        
    def identifyProcedure(self, WordDocList, ProcedureStrings, SubProcedureStrings):
        begin = -1
        end = -1
        index = 0
        Resets1Index = 0
        print(ProcedureStrings)
        print(SubProcedureStrings)
        x = 0
        while x < len(self.Resets0):
            while(index < len(WordDocList) and len(ProcedureStrings) > 0):
                if isinstance(WordDocList[index], TextualElement) and WordDocList[index].getRunsText() == ProcedureStrings[0]:
                    begin = index
                    Resets1Index = 0
                    y = 0
                    while(index < len(WordDocList) and y < self.Resets0[x]):
                        if isinstance(WordDocList[index], TextualElement) and WordDocList[index].getRunsText() == ProcedureStrings[0]:
                            ProcedureStrings.pop(0)
                            y += 1
                            z = 0
                            while(index < len(WordDocList) and z < self.Resets1[Resets1Index]):
                                if isinstance(WordDocList[index], TextualElement) and WordDocList[index].getRunsText() == SubProcedureStrings[0]:
                                    SubProcedureStrings.pop(0)
                                    z += 1
                                index += 1
                        index += 1
                        Resets1Index += 1
                    if self.Resets1[Resets1Index - 1] > 0:
                        index = index - 1
                    end = index
                    print(begin, end)
                    index = self.extractProcedure(WordDocList, begin, end)
                elif (isinstance(WordDocList[index], Table)):
                    self.identifyTableProcedure(WordDocList, ProcedureStrings)
                index += 1
            x += 1
        
    def extractProcedure(self, WordDocList, begin, end):
        procedure = Procedure([],"",0, 0) #procedure instance
        procedure.setProcedureName(WordDocList[begin].getRuns()[0].getText())
        procedure.setLineNumber(WordDocList[begin].getLineNumber())
        procedure.setNumberOfSteps(end - begin)
        for x in range(end - begin): #iterate through the elements that belong to the procedure 
            procedure.appendElement(WordDocList.pop(begin)) #append the element at spot index to the procedure and remove it from the list.
        WordDocList.insert(begin, procedure) #add the procedure to the WordDocList
        return begin
