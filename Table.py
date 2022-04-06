from Column import *
from Row import *
from Cell import *

class Table():
    def __init__(self, columnsList, rowsList, cellsList, numColumnsInt, numRowsInt, lineInt, sectionString, tableNameString):
        self.columns = columnsList
        self.rows = rowsList
        self.cells = cellsList
        self.numberOfColumns = numColumnsInt
        self.numberOfRows = numRowsInt
        self.lineNumber = lineInt
        self.sectionOfDocument = sectionString
        self.tableName = tableNameString

    def getColumns(self):
        return self.columns

    def getRow(self):
        return self.rows

    def getCells(self):
        return self.cells

    def getNumberOfColumns(self):
        return self.numberOfColumns

    def getNumberOfRows(self):
        return self.numberOfRows
    
    def getLineNumber(self):
        return self.lineNumber

    def getSectionOfDocument(self):
        return self.sectionOfDocument

    def getTableName(self):
        return self.tableName

    def setColumns(self, columnsArg):
        self.columns = columnsArg

    def setRows(self, rowsArg):
        self.rows = rowsArg

    def setCells(self, cellsArg):
        self.cells = cellsArg

    def setNumberOfColumns(self, numberOfColumnsArg):
        self.numberOfColumns = numberOfColumnsArg

    def setNumberOfRows(self, numberOfRowsArg):
        self.numberOfRows = numberOfRowsArg
        
    def setLineNumber(self, lineNumberArg):
        self.lineNumber = lineNumberArg

    def setSectionOfDocument(self, sectionOfDocumentArg):
        self.sectionOfDocument = sectionOfDocumentArg

    def setTableNameArg(self, TableNameArg):
        self.tableName = TableNameArg

    #Identify and add collums rows and cells
    def appendColumn(self, column):
        self.columns.append(column)

    def appendRow(self, row):
        self.rows.append(row)

    def appendCell(self, cell):
        self.cells.append(cell)
        
    def identifyTable(self, lineNumber):
        return True

    def extractTable(self, lineNumber):
        return True
    
    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
