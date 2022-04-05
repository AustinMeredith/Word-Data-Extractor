class Column():
    def __init__(self):
        self.tableName = ""
        self.columnName = ""
        self.numberOfCells = 0

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
    
    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
