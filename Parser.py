import docx
from TextualElement import *
#import GraphicalElement
#import Table
#import Row
#import Cell
#import Procedure

class Parser():
    def __init__(self, docName):
        #Replace with filepath for whatever document
        self.doc = docx.Document(docName) 
        self.all_paras = self.doc.paragraphs
        sections = self.doc.sections
        self.firstPageHeader = sections[0].first_page_header 
        self.firstPageFooter = sections[0].first_page_footer
        self.header = sections[0].header
        self.footer = sections[0].footer


# Method definitions

# Text Methods -------------------------------------------------------------

    def findHBF(self, para):
        headerParagraphs = self.header.paragraphs + self.firstPageHeader.paragraphs
        for headerPara in headerParagraphs:
            if para.text == headerPara.text:
                return 1
        footerParagraphs = self.footer.paragraphs + self.firstPageFooter.paragraphs
        for footerPara in footerParagraphs:
            if para.text == footerPara.text:
                return 2
        return 0

    def findRuns(self, para):
        runsArray = []
        for run in para.runs:
            runsArray.append(run.text)
        return runsArray

#def findSection(para):

#Run Methods -----------------------------------------------------------

    def findText(self, run):
        runText = run.text
        return runText
    
    def findBold(self, run):
        if run.bold:
           return bool(True)
        else:
           return bool(False)

    def findFont(self, run):
        if not(run.font.name is None):
            return run.font.name
        elif not(run.style.font.name is None):
            return run.style.font.name
        else:
            return "Unknown"

    def findItalic(self, run):
        if run.italic:
            return bool(True)
        else:
            return bool(False)

    def findStyle(self, run):
        if not(run.style.name is None):
            return run.style.name
        else:
            return "Unknown"

    def findUnderline(self, run):
        if run.underline:
            return bool(True)
        else:
            return bool(False)

#Table Methods ---------------------------------------------------------

    def findColumnList(self, table):
        columnList = []
        columnText = []
        for column in table.columns:
            for cell in column.cells:
                for para in cell.paragraphs:
                    columnText.append(para.text)
            columnList.append(columnText)
            columnText = []
        return columnList

    def findRowsList(self, table):
        rowsList = []
        rowText = []
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    rowText.append(para.text)
            rowsList.append(rowText)
            rowText = []
        return rowsList 
 
    def findCellsList(self, table):
        cellsList = []
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    cellsList.append(para.text)
       
    def findNumOfColumns(self, table):
        numOfColumns = 0
        for column in table.columns:
            numOfColumns += 1
        return numOfColumns

    def findNumOfRows(self, table):
        numOfRows = 0
        for row in table.rows:
            numOfRows += 1
        return numOfRows

#def findLineNumber

    def findTableName(self, table):
        tableName = ""
        if table.rows[0].cells[0].text and table.rows[0].cells[0].text.strip():
            tableName += table.rows[0].cells[0].text
        else:
            tableName += table.rows[0].cells[1].text
        return tableName

#Row Methods -----------------------------------------------------------

    def findRowString(self, row):
        rowString = ""
        for cell in row.cells:
            for para in cell.paragraphs:
                rowString += para.text
                rowString += " "
        return rowString

    def findTable(self, row):
        return row.table


    def findNumOfCells(self, row):
        cellCount = 0
        for cell in row.cells:
            cellCount += 1
        return cellCount


#Cell Methods -----------------------------------------------------------------

    def c_findText(self, cell):
        cellText = ""
        for para in cell.paras:
            cellText += para.text
        return cellText

    def paragraphParse(self):
        textualElementList = []
        iteration = 0
        for para in self.all_paras:
            if(len(para.runs) > 0 and para.runs[0].text != ""):
                textualElementList.append(TextualElement(iteration, self.findHBF(para), para.style.name, []))
                numRuns = 0
                for run in para.runs:
                    if numRuns > 0 :
                        run0 = textualElementList[iteration].getRun(numRuns - 1)
                        if (run0.getFont() == self.findFont(run) and run0.getStyle() == self.findStyle(run) and run0.getBold() == self.findBold(run) and run0.getItalic() ==  self.findItalic(run) and run0.getUnderline() == self.findUnderline(run)):
                            run0.appendText(self.findText(run))
                        else:
                            textualElementList[iteration].appendRun(Run(consecutiveRuns, self.findFont(run), self.findStyle(run), self.findBold(run), self.findItalic(run), self.findUnderline(run)))
                            numRuns += 1
                    else:
                        textualElementList[iteration].appendRun(Run(self.findText(run), self.findFont(run), self.findStyle(run), self.findBold(run), self.findItalic(run), self.findUnderline(run)))
                        numRuns += 1
                iteration += 1
        return textualElementList
