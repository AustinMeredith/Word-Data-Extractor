#Note 1 the removeHyperLinks method removes the tags surrounding hyperlinks in the list provided by docx2pyton.document.body, but leaves the text that the hyperlink was associated with.
#The problem lies in that python-docx can't see hyperlinks at all, so when parsing the document with the Parser class (which uses python-docx) those hyperlinks are invisible, and thus aren't recorded as textual elements.
#That's why it's necessary to remove hyperlinks.
#Note 2 Text boxes, whether integrated into the text, or as inline shapes, python-docx can't detect those text boxes, and thus they aren't recorded as textual elements. Thus, it's necessary to remove text boxes.
#Note 3 Certain characters that appear in Word are not compatable with the encoding of the XML output (UTF-8), and thus must be removed.
from docx2python.iterators import enum_at_depth
from docx2python.iterators import enum_cells

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
