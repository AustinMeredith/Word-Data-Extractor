from docx2python import docx2python
from docx2python.iterators import enum_at_depth
from ProcedureParser import *
'''
    Tokens0 and Tokens1 in Assembly procedure (Actual numbered list) Tokens1 sublevel of Tokens0
    Tokens2 and Tokens3 in t-u5-12-T3.docx

    postPattern =  ")\\t\\t" for Tokens0
    prePattern = "\\t" postPattern = ")\\t\\t" for Tokens1
    postPattern = ".\\t" for Tokens2
    prePattern = "\\t" postPattern = ".\\t" for Tokens3
'''
ProcedureParser = ProcedureParser()
ProcedureParser.generateTokens0("", ")\t\t")
ProcedureParser.generateTokens1("\t", ")\t\t")
document = docx2python("C:/Users/marti/Desktop/Word Data Extraction/4-15/Order/TestDocs/Assembly Procedure-T1.docx")
docTables = document.body
ProcedureParser.removeEmptyParagraphs(docTables)
ProcedureParser.identifyProcedureStrings(docTables)
for x in ProcedureParser.ProcedureStrings:
    print(x)
for x in ProcedureParser.SubProcedureStrings:
    print(x)
#for (i,j,k,l), paragraph in enum_at_depth(tables, 4):
    #print(tables[i][j][k][l])
#print(tables)
'''Method for extracting procedures, though convoluted: use this to identify them in the document, then compare that against
the extracted paragraphs in our class structure. Use that to decide which paragraphs to pull as procedures'''

'''for token in Tokens0:
    print(token)

for token in Tokens1:
    print(token)'''
    
'''for x in range(len(document.body)):
    print(str(document.body[x]) + "\n")'''

'''


document.body[2][0][0][2]'''
