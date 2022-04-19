from Column import *
from Row import *
from Cell import *

class Table():
    def __init__(self, columnsList, rowsList, cellsList, numColumnsInt, numRowsInt, lineInt, tableNameString):
        self.columns = columnsList
        self.rows = rowsList
        self.cells = cellsList
        self.numberOfColumns = numColumnsInt
        self.numberOfRows = numRowsInt
        self.lineNumber = lineInt
        self.tableName = tableNameString

    def getColumns(self):
        return self.columns

    def getRows(self):
        return self.rows

    def getCells(self):
        return self.cells

    def getNumberOfColumns(self):
        return self.numberOfColumns

    def getNumberOfRows(self):
        return self.numberOfRows
    
    def getLineNumber(self):
        return self.lineNumber

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

    def setTableName(self, TableNameArg):
        self.tableName = TableNameArg

    #Identify and add collums rows and cells
    def appendColumn(self, column):
        self.columns.append(column)

    def appendRow(self, row):
        self.rows.append(row)

    def appendCell(self, cell):
        self.cells.append(cell)

    def indent(self, indentAmt): #Used in XMLReturn returns spaces for indentation
        indentation = ""
        for x in range(indentAmt):
            indentation += "  "
        return indentation
    
    def XMLReturn(self, indentAmt): #Returns XML Code for this object as a string
        xml = ""
        xml += self.indent(indentAmt)
        xml += "<Table"
        xml += " TableName=\"" + self.tableName
        xml += "\" LineNumber=\"" + str(self.lineNumber)
        xml += "\" NumberOfRows=\"" + str(self.numberOfRows)
        xml += "\" NumberOfColumns=\"" + str(self.numberOfColumns) + "\">"
        for cell in self.cells:
            xml += "\n"
            xml += cell.XMLReturn(indentAmt + 1)
        for row in self.rows:
            xml += "\n"
            xml += self.indent(indentAmt + 1)
            xml += row.XMLReturn()
        for column in self.columns:
            xml += "\n"
            xml += self.indent(indentAmt + 1)
            xml += column.XMLReturn()
        xml += "\n"
        xml += self.indent(indentAmt)
        xml += "</Table>"
        return xml
