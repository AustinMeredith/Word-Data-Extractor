class Column():
    def __init__(self, tableString, columnString, cellsInt):
        self.tableName = tableString
        self.columnName = columnString
        self.numberOfCells = cellsInt

    def getTableName(self):
        return self.tableName

    def getColumnName(self):
        return self.columnName

    def getNumberOfCells(self):
        return self.numberOfCells

    def setTableName(self, tableNameArg):
        self.tableName = tableNameArg

    def setColumnName(self, columnNameArg):
        self.columnName = columnNameArg

    def setNumberOfCells(self, numberOfCellsArg):
        self.numberOfCells = numberOfCellsArg
    
    def XMLReturn(self): #Returns the XML Code for this object as a string.
        xml = "<Column"
        xml += " TableName=\"" + self.tableName
        xml += "\" Name=\"" + self.columnName
        xml += "\" NumberOfCells=\"" + str(self.numberOfCells) + "\"/>"
        return xml
