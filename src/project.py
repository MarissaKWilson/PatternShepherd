class project:

    def __init__(self, projectName):
        self.patterns = []
        self.currentRow = 0
        self.projectName = projectName

    def readRow(self, rowNum):
        row = []
        for p in self.patterns:
            row.append(', '.join(p.get_row(rowNum)))
            row.append('pm')
        row.pop(len(row)-1)
        rowStr = ', '.join(row)
        return rowStr

    def nextRow(self):
        self.currentRow+=1
        data = [self.currentRow, self.readRow(self.currentRow)]
        return data

    def lastRow(self):
        self.currentRow-=1
        data = [self.currentRow, self.readRow(self.currentRow)]
        return data

    def addPattern(self, pattern):
        self.patterns.append(pattern)