from Run import *
from TextualElement import *
from GraphicalElement import *
from Cell import *
from Row import *
from Column import *
from Table import *
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

#Textual Element Instance
textualElementInstance = TextualElement(0,0,"",[])
textualElementInstance.setLineNumber(52)
textualElementInstance.setHeaderFooterBody(1)
textualElementInstance.setSectionOfDocument("Body")
textualElementInstance.appendRun(runInstance)
textualElementInstance.appendRun(runInstance2)
textualElementInstance.appendRun(runInstance3)

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
print(tableInstance.XMLReturn(0))
