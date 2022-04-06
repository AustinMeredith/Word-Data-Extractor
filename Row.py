class Row():
    def __init__(self, tableString, rowString, cellsInt):
        self.tableName = tableString
        self.rowName = rowString
        self.numberOfCells = cellsInt

    def getTableName(self):
        return self.tableName

    def getRowName(self):
        return self.rowName

    def getNumberOfCells(self):
        return self.numberOfCells

    def setTableName(self, tableNameArg):
        self.tableName = tableNameArg

    def setRowName(self, rowNameArg):
        self.rowName = rowNameArg

    def setNumberOfCells(self, numberOfCellsArg):
        self.numberOfCells = numberOfCellsArg
    
    def XMLReturn(self): #Unimplemented working on it next few days
        return ""
