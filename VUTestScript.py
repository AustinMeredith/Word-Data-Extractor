from VariableUtility import *
vu = VariableUtility()
#3 valid inputs
print(vu.setOutputFileLocation("C:/Users/marti/Desktop/Word Data Extraction"))
print(vu.setOutputFileName("Jello.xml"))
print(vu.setInputFilePath("C:/Users/marti/Desktop/Word Data Extraction/Test.docx"))
print(vu.getOutputFileLocation())
print(vu.getOutputFileName())
print(vu.getInputFilePath())
#4 invalid inputs
print(vu.setOutputFileLocation("nullfighter"))
print(vu.setOutputFileName("flashbang"))
print(vu.setOutputFileName("C:/Users/marti/Desktop/Word Data Extraction/New.txt"))
print(vu.setOutputFileName("C:/Users/marti/Desktop/Word Data Extraction/Nude.docx"))
