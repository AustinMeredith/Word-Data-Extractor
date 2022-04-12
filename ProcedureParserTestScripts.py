from Run import *
from TextualElement import *
from GraphicalElement import *
from Cell import *
from Row import *
from Column import *
from Table import *
from Procedure import *
from VariableUtility import *
from ProcedureParser import *

#procedure parser to be tested
proparser = ProcedureParser()

#using VariableUtility for its intended purpose
vu = VariableUtility()
vu.setOutputFileLocation("C:/Users/marti/Desktop/Word Data Extraction/XMLReturns")
vu.setOutputFileName("Matters.xml")
vu.setInputFilePath("C:/Users/marti/Desktop/Word Data Extraction/Test.docx")

#To be used for storing instances of objects with XMLReturn() method. 
WordDocList = []

#Creating 3 Run instances
#Run Instance 1
runInstance = Run("",False,"",False,"",False)
runInstance.setText("Nothing really matters.")
runInstance.setBold(False)
runInstance.setFont("Impact")
runInstance.setItalic(False)
runInstance.setStyle("Body")
runInstance.setUnderline(True)

#Run Instance 2
runInstance2 = Run("",False,"",False,"",False)
runInstance2.setText("I think all things do.")
runInstance2.setBold(False)
runInstance2.setFont("Calibri")
runInstance2.setItalic(True)
runInstance2.setStyle("Body")
runInstance2.setUnderline(False)

#Run Instance 3
runInstance3 = Run("",False,"",False,"",False)
runInstance3.setText("There are some things that do.")
runInstance3.setBold(False)
runInstance3.setFont("Times New Roman")
runInstance3.setItalic(True)
runInstance3.setStyle("Body")
runInstance3.setUnderline(False)

#Name Instance
nameInstance = Run("Assembly Procedure", False, "Calibri", False, "Body",False)

#NumberRun1
numRun1 = Run("",False,"",False,"",False)
numRun1.setText("1.1\tAssemble 12901531 Key Insert into 13015691 Wing Knob until inserted to 0.3 + 0.5 mm below surface as shown on drawing 13015690 Wing Knob Assembly. (Figure 1)")
numRun1.setBold(False)
numRun1.setFont("Times New Roman")
numRun1.setItalic(True)
numRun1.setStyle("Body")
numRun1.setUnderline(False)

#NumberRun2
numRun2 = Run("1.2\tInsert pins flush with 12901531 Key Insert body to permanently lock in place. (Figure 1)",False,"Calibri",False,"Body",False)

#Textual Element Instances
textualElementInstance = TextualElement(0,0,"",[])
textualElementInstance.setLineNumber(52)
textualElementInstance.setHeaderFooterBody(1)
textualElementInstance.setSectionOfDocument("Body")
textualElementInstance.appendRun(runInstance)
textualElementInstance.appendRun(runInstance2)
textualElementInstance.appendRun(runInstance3)

textualElementInstance2 = TextualElement(53, 1, "Body", [runInstance2, runInstance3])
nameTextualElementInstance = TextualElement(54, 1, "Body", [nameInstance])
numTextualElementInstance1 = TextualElement(55, 1, "Body", [numRun1])
numTextualElementInstance2 = TextualElement(56, 1, "Body", [numRun2])

#Graphical Element Instance (Condensed since I allowed constructors to have parameters)
graphicalElementInstance = GraphicalElement(0, 1, "Cell", "C:/Users/marti/Desktop/DS ROMS/Hacking/4998 - Pokemon - Platinum Version (v01) (U).sav")

#Row Instance
rowInstance0 = Row("Unknown", "Row0", 1)
rowInstance1 = Row("Unknown", "Row1", 1)
rowInstance2 = Row("Unknown", "Row2", 1)

#Column Instance
columnInstance = Column("Unknown", "Person", 3)

#Cell Instance
cellInstance0 = Cell([textualElementInstance], [graphicalElementInstance], "Unknown", 0, 0)
cellInstance1 = Cell([], [], "Unknown", 0, 1)
cellInstance2 = Cell([], [], "Unknown", 0, 2)

#Table Instance
tableInstance = Table([columnInstance],
                     [rowInstance0, rowInstance1, rowInstance2],
                     [cellInstance0, cellInstance1, cellInstance2],
                      1, 3, 11,
                      "Body", "Unknown")

#Procedure Instance
procedureInstance = Procedure([textualElementInstance],
                              "What Matters", 51, "Body", 1)

#Adding all elements to the WordDocList
WordDocList.append(textualElementInstance)
WordDocList.append(tableInstance)
WordDocList.append(graphicalElementInstance)
WordDocList.append(procedureInstance)
WordDocList.append(textualElementInstance2)
WordDocList.append(nameTextualElementInstance)
WordDocList.append(numTextualElementInstance1)
WordDocList.append(numTextualElementInstance2)
WordDocList.append(textualElementInstance)

proparser.generateTokens()
proparser.identifyProcedure(WordDocList)

'''x = none
if not(x is None):
    print("x is not None")'''
    
'''for element in WordDocList:
    print((isinstance(element , TextualElement)))'''

#The following code should be implemented as part of the Interpreter or Parser when we need to save the XML
xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n<WordDoc\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:noNamespaceSchemaLocation=\"DEO3.xsd\">\n"
for element in WordDocList:
    xml += element.XMLReturn(1)
    xml += "\n"
xml +="</WordDoc>"
#outputFile = open(vu.getOutputFileLocation() + "/" + vu.getOutputFileName(), "wt")
#outputFile.write(xml)
#outputFile.close()
print(xml)
    
